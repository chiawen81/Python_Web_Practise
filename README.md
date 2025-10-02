# Python_Web_practise

本專案示範多個 Flask 教學範例，建議使用 uv 或虛擬環境執行。

快速開始（Windows PowerShell）
- 建立與啟用虛擬環境：`python -m venv .venv && .venv\Scripts\activate`
- 安裝套件：`pip install -r requirements.txt`
- 執行主程式：`python main.py`

範例課程位於 `lesson*` 目錄，可依需求進入對應資料夾啟動。

使用 uv（可選，建議）
- 安裝 uv（若尚未安裝）：請見 https://docs.astral.sh/uv/
- 同步依賴：`uv sync`
- 執行主程式：`uv run python main.py`
- 執行課程範例：
  - lesson4（App Factory）：`uv run python .\lesson4\app.py`
  - lesson5（含模板/靜態資源）：`uv run python .\lesson5\app.py`
