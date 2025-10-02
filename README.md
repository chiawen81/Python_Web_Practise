# Python_Web_practise

?砍?獢內蝭???Flask ?飛蝭?嚗遣霅唬蝙??uv ???祉憓銵?
敹恍?憪?Windows PowerShell嚗?- 撱箇????刻??祉憓?`python -m venv .venv && .venv\Scripts\activate`
- 摰?憟辣嚗pip install -r requirements.txt`
- ?瑁?銝餌?撘?`python main.py`

蝭?隤脩?雿 `lesson*` ?桅?嚗靘?瘙脣撠?鞈?憭曉???
雿輻 uv嚗?賂?撱箄降嚗?- 摰? uv嚗撠摰?嚗?隢? https://docs.astral.sh/uv/
- ?郊靘陷嚗uv sync`
- ?瑁?銝餌?撘?`uv run python main.py`
- ?瑁?隤脩?蝭?嚗?  - lesson4嚗pp Factory嚗?`uv run python .\lesson4\app.py`
  - lesson5嚗璅⊥/??鞈?嚗?`uv run python .\lesson5\app.py`

## 連線外部 MCP Server（Chrome / Codex）

此專案提供 Codex 端連線外部 Chrome MCP server 的設定樣板（僅設定與說明，未包含 server 實作）。

前置：啟動 Chrome Remote Debugging
- Windows PowerShell 範例：
  - `& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="$env:LOCALAPPDATA\ChromeMCP"`

Codex 連線設定（stdio 推薦）
- 樣板檔：`mcp/clients/codex.mcp.json`
- 內容重點：
  - `command`: `python`
  - `args`: `[-m, your_mcp_chrome]`（請以實際 server 模組替換）
  - `env.CHROME_REMOTE_URL`: `http://127.0.0.1:9222`
  - `env.CHROME_PROFILE`: `%LOCALAPPDATA%/ChromeMCP`
  - `transport`: `stdio`

Codex 使用流程
- 在 Codex CLI/Chat 匯入或指定 `mcp/clients/codex.mcp.json`。
- 啟動對話後，Codex 會以 stdio 啟動 `your_mcp_chrome`。
- 可實作並呼叫以下工具（建議）：
  - `chrome.list_tabs`, `chrome.active_tab_info`, `chrome.screenshot`
  - `chrome.get_dom_outer_html`, `chrome.get_console_logs`, `chrome.get_network_summary`

疑難排解
- 連線失敗：確認 Chrome 以 `--remote-debugging-port=9222` 啟動。
- 權限/路徑：確認 Chrome 安裝路徑與 `user-data-dir` 可寫入。
- Server 未實作：此倉庫目前僅提供 Codex 連線樣板；如需，我可協助實作最小版 Python Chrome MCP server。
