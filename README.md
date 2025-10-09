# Python_Web_practise

這是一個基於 Flask 的練習專案，使用 uv 進行套件與虛擬環境管理。

## 環境設置

1. 建立虛擬環境並啟用：
   - Windows PowerShell:
     ```powershell
     python -m venv .venv && .venv\Scripts\activate
     ```
2. 安裝相依套件：
   ```powershell
   pip install -r requirements.txt
   ```
3. 啟動專案：
   ```powershell
   python main.py
   ```

## Lesson 說明

各個 `lesson*` 資料夾包含不同的練習內容：

- 使用 uv:
  1. 同步套件：
     ```powershell
     uv sync
     ```
  2. 啟動專案：
     ```powershell
     uv run python main.py
     ```
  3. 啟動特定 Lesson：
     - Lesson 4 (App Factory):
       ```powershell
       uv run python .\lesson4\app.py
       ```
     - Lesson 5 (完整範例/作業):
       ```powershell
       uv run python .\lesson5\app.py
       ```

## 連線外部 MCP Server（Chrome / Codex）

此專案提供 Codex 端連線外部 Chrome MCP server 的設定樣板（僅設定與說明，未包含 server 實作）。

### 前置：啟動 Chrome Remote Debugging

- Windows PowerShell 範例：
  ```powershell
  & "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="$env:LOCALAPPDATA\ChromeMCP"
  ```

### Codex 連線設定（stdio 推薦）

- 樣板檔：`mcp/clients/codex.mcp.json`
- 內容重點：
  - `command`: `python`
  - `args`: `[-m, your_mcp_chrome]`（請以實際 server 模組替換）
  - `env.CHROME_REMOTE_URL`: `http://127.0.0.1:9222`
  - `env.CHROME_PROFILE`: `%LOCALAPPDATA%/ChromeMCP`
  - `transport`: `stdio`

### Codex 使用流程

1. 在 Codex CLI/Chat 匯入或指定 `mcp/clients/codex.mcp.json`。
2. 啟動對話後，Codex 會以 stdio 啟動 `your_mcp_chrome`。
3. 可實作並呼叫以下工具（建議）：
   - `chrome.list_tabs`, `chrome.active_tab_info`, `chrome.screenshot`
   - `chrome.get_dom_outer_html`, `chrome.get_console_logs`, `chrome.get_network_summary`

### 疑難排解

- 連線失敗：確認 Chrome 以 `--remote-debugging-port=9222` 啟動。
- 權限/路徑：確認 Chrome 安裝路徑與 `user-data-dir` 可寫入。
- Server 未實作：此倉庫目前僅提供 Codex 連線樣板；如需，我可協助實作最小版 Python Chrome MCP server。
