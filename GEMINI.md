# Gemini Agent 指南

本文件為 Gemini agent 在此儲存庫中工作時提供指引。

## 專案概覽

這是一個使用 Flask 框架的 Python 網頁開發學習專案。專案被組織成多個課程（`lesson1` 到 `lesson5`），每個課程都展示了不同的 Flask 概念。**uv** 用於虛擬環境和套件管理。

## 主要指令

1.  **預設語言**：根據儲存庫的通用指南，請在所有回覆、註解和文件中使用**正體中文**。

2.  **套件管理**：本專案使用 **uv**。所有套件安裝和腳本執行都應透過 `uv` 處理。
    - 安裝/同步依賴：`uv sync`
    - 執行腳本：`uv run python <script_path.py>`

3.  **執行應用程式**：
    - 執行主應用程式：`uv run python main.py`
    - 執行特定課程的應用程式（例如，lesson 4）：`uv run python .\lesson4\app.py`

4.  **程式碼風格與品質**：
    - 遵守現有的程式碼風格。
    - 在最終確定變更之前，使用 `ruff check .` 進行 linting，並使用 `ruff format .` 進行格式化。
    - 遵循 `AGENTS.md` 中使用 `pytest` 的測試指南。

5.  **架構模式**：
    - 注意專案中使用的兩種主要 Flask 應用程式結構：
        1.  **簡單模式**：單一 `app.py` 檔案（例如，`main.py`, `lesson5/app.py`）。
        2.  **應用程式工廠模式**：使用 `create_app()` 函式（例如，`lesson4/app.py`）。
    - 修改檔案時，請符合現有的模式。

6.  **通用指南**：關於測試、提交訊息和安全性等更廣泛的儲存庫慣例，請隨時參考 `AGENTS.md`。
