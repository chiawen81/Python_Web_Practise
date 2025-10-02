import asyncio
import json
import os
import sys
from typing import Any, Dict, List, Optional

import httpx
import websockets

class JsonRpcStdio:
    def __init__(self):
        self.reader = asyncio.StreamReader()
        self.protocol = asyncio.StreamReaderProtocol(self.reader)
        self.transport = None
        self.writer = None

    async def setup_stdio(self):
        loop = asyncio.get_running_loop()
        await loop.connect_read_pipe(lambda: self.protocol, sys.stdin)
        self.transport, _ = await loop.connect_write_pipe(asyncio.streams.FlowControlMixin, sys.stdout)
        self.writer = asyncio.StreamWriter(self.transport, self.protocol, self.reader, loop)

    async def send(self, obj: Dict[str, Any]):
        data = (json.dumps(obj) + "\n").encode("utf-8")
        self.writer.write(data)
        await self.writer.drain()

    async def recv(self) -> Dict[str, Any]:
        line = await self.reader.readline()
        if not line:
            raise EOFError
        return json.loads(line.decode("utf-8"))

class ChromeClient:
    def __init__(self, remote_url: Optional[str] = None):
        self.remote_url = remote_url or os.getenv("CHROME_REMOTE_URL", "http://127.0.0.1:9222")

    async def _fetch_json(self, path: str):
        async with httpx.AsyncClient(timeout=5.0) as client:
            r = await client.get(self.remote_url.rstrip("/") + path)
            r.raise_for_status()
            return r.json()

    async def list_tabs(self) -> List[Dict[str, Any]]:
        data = await self._fetch_json("/json")
        tabs = [
            {"id": t.get("id"), "title": t.get("title"), "url": t.get("url"), "webSocketDebuggerUrl": t.get("webSocketDebuggerUrl")}
            for t in data if t.get("type") == "page"
        ]
        return tabs

    async def get_active_target(self) -> Optional[Dict[str, Any]]:
        tabs = await self.list_tabs()
        return tabs[0] if tabs else None

    async def capture_screenshot_base64(self, ws_url: str) -> str:
        async with websockets.connect(ws_url, max_size=20*1024*1024) as ws:
            msg_id = 1
            await ws.send(json.dumps({"id": msg_id, "method": "Page.enable"}))
            await ws.recv()
            msg_id += 1
            await ws.send(json.dumps({"id": msg_id, "method": "Page.bringToFront"}))
            await ws.recv()
            msg_id += 1
            await ws.send(json.dumps({"id": msg_id, "method": "Page.captureScreenshot", "params": {"format": "png"}}))
            while True:
                raw = await ws.recv()
                obj = json.loads(raw)
                if obj.get("id") == msg_id and "result" in obj:
                    return obj["result"].get("data", "")
        return ""

class McpServer:
    def __init__(self):
        self.rpc = JsonRpcStdio()
        self.chrome = ChromeClient()

    def _result(self, id_: int, result: Any):
        return {"jsonrpc": "2.0", "id": id_, "result": result}

    def _error(self, id_: Optional[int], code: int, message: str):
        return {"jsonrpc": "2.0", "id": id_, "error": {"code": code, "message": message}}

    async def handle(self, msg: Dict[str, Any]):
        method = msg.get("method")
        id_ = msg.get("id")
        params = msg.get("params") or {}

        if method == "initialize":
            return await self.rpc.send(self._result(id_, {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": True}
            }))

        if method == "tools/list":
            tools = [
                {"name": "chrome.list_tabs", "description": "List open Chrome tabs"},
                {"name": "chrome.active_tab_info", "description": "Get active tab info"},
                {"name": "chrome.screenshot", "description": "Capture active tab screenshot (base64)"}
            ]
            return await self.rpc.send(self._result(id_, {"tools": tools}))

        if method == "tools/call":
            name = params.get("name")
            args = params.get("arguments") or {}
            try:
                if name == "chrome.list_tabs":
                    res = await self.chrome.list_tabs()
                    return await self.rpc.send(self._result(id_, {"content": res}))
                if name == "chrome.active_tab_info":
                    tab = await self.chrome.get_active_target()
                    return await self.rpc.send(self._result(id_, {"content": tab}))
                if name == "chrome.screenshot":
                    tab = await self.chrome.get_active_target()
                    if not tab or not tab.get("webSocketDebuggerUrl"):
                        return await self.rpc.send(self._error(id_, -32000, "No active tab or missing WebSocket URL"))
                    data = await self.chrome.capture_screenshot_base64(tab["webSocketDebuggerUrl"])
                    return await self.rpc.send(self._result(id_, {"content": {"mime": "image/png", "base64": data}}))
                return await self.rpc.send(self._error(id_, -32601, f"Unknown tool: {name}"))
            except httpx.HTTPError as e:
                return await self.rpc.send(self._error(id_, -32001, f"HTTP error: {e}"))
            except Exception as e:
                return await self.rpc.send(self._error(id_, -32000, str(e)))

        return await self.rpc.send(self._error(id_, -32601, f"Unknown method: {method}"))

    async def run(self):
        await self.rpc.setup_stdio()
        while True:
            try:
                msg = await self.rpc.recv()
                await self.handle(msg)
            except EOFError:
                break

async def main():
    server = McpServer()
    await server.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
