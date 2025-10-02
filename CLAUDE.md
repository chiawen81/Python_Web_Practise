# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 專案概述

這是一個基於 Flask 的 Python 網頁開發學習專案，使用 **uv** 進行套件與虛擬環境管理。專案包含多個課程（lesson1-5），展示從基礎路由到模板系統的漸進式 Flask 概念。

## 常用指令

### 執行應用程式
- **執行任何 Flask 應用**: `uv run python ./lessonX/app.py`（將 X 替換為課程編號）
- **執行主應用**: `uv run python main.py`
- **安裝相依套件**: `uv sync` 或 `uv pip install -r requirements.txt`

### 套件管理
本專案使用 **uv** 而非 pip 進行套件管理。所有 Python 指令都應加上 `uv run` 前綴。

## 架構說明

### 專案結構
- **lesson1-3**: Jupyter notebooks（`.ipynb`）- Python/Flask 入門概念
- **lesson3**: 包含使用 `requests` 進行 API 資料抓取的範例
- **lesson4**: 使用 App Factory 模式（`create_app()`）的 Flask 應用，模板使用繼承機制（`base.html`）
- **lesson4-2**: 簡化版的 Flask 應用結構
- **lesson5**: 包含模板與靜態資源（CSS、JS、圖片）的 Flask 應用

### Flask 應用程式模式

**專案中使用兩種模式：**

1. **簡單模式**（main.py, lesson5/app.py）:
   ```python
   app = Flask(__name__)

   @app.route("/")
   def index():
       return render_template("index.html")

   if __name__ == "__main__":
       app.run(debug=True)
   ```

2. **App Factory 模式**（lesson4/app.py）:
   ```python
   def create_app() -> Flask:
       app = Flask(__name__)

       @app.route("/")
       def home():
           return render_template("index.html")

       return app

   app = create_app()
   ```

### 模板與靜態檔案
- **模板檔案**: Flask 使用各課程目錄下的預設 `templates/` 資料夾
- **靜態資源**（CSS、JS、圖片）: 使用各課程目錄下的 `static/` 資料夾
- **模板繼承**: lesson4 展示了使用 `base.html` 的基礎模板繼承機制

## 開發規範（來自 .copilot/instructions.md）

### 程式架構
- 較大專案優先採用 Flask App Factory + Blueprint 模式
- 避免將所有邏輯寫在單一檔案
- 遵循 PEP8 與 PEP20 標準
- 使用 snake_case 命名規範

### 資料庫與 ORM
- 使用 SQLAlchemy 作為 ORM
- 使用 Flask-Migrate 進行 schema 遷移

### 配置管理
- 使用 `config.py` 或 `.env` 管理環境變數
- 避免硬編碼配置

### API 設計
- 遵循 RESTful 規範
- 必要時使用 Marshmallow 進行序列化/驗證

### 測試
- 所有範例程式碼開頭需加上 `# WenTest` 註解
- 使用 pytest 撰寫單元測試（放置於 `tests/` 目錄）

### 輸出格式
- 程式碼需完整且可執行
- 註解與說明使用繁體中文
- 集中管理 Exception Handler，回傳 JSON 格式錯誤訊息
