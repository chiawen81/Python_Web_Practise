# Repository Guidelines

本指南說明如何在本儲存庫中高效協作。

## 專案結構與模組組織
- `src/` – 主要 Python 套件與模組（應用程式程式碼）。
- `tests/` – 與 `src/` 結構對應的單元／整合測試。
- `assets/` – 靜態檔（範例資料、圖片）如適用。
- `scripts/` – 輔助指令（設定、維護）。
- 使用套件內 `__init__.py`；模組應小而聚焦。

## 建置、測試與開發指令
- `python -m venv .venv && .venv\\Scripts\\activate` – 建立並啟用虛擬環境（Windows PowerShell）。
- `pip install -r requirements.txt` – 安裝執行期相依。
- `pip install -r requirements-dev.txt` – 安裝開發／測試工具。
- `pytest -q` – 安靜模式執行測試。
- `pytest -q --maxfail=1 -k name` – 針對部分測試快速迭代。
- `python -m src.<entry_module>` – 本機執行應用（將 `<entry_module>` 替換為實際模組）。
 - 使用 `uv`（可選，建議）：
   - `uv sync` – 同步依賴
   - `uv run python main.py` – 執行主程式
   - `uv run python .\\lesson4\\app.py`、`uv run python .\\lesson5\\app.py` – 執行對應課程範例

## 程式風格與命名慣例
- Python 3.10+；4 空白縮排；UTF‑8。
- 命名：套件／模組使用 `snake_case`；類別 `PascalCase`；函式／變數 `snake_case`；常數 `UPPER_SNAKE_CASE`。
- 公開函式／類別需加入型別註解。
- Lint/格式化：`ruff check .`、`ruff format .`（或使用 `black .`）。提交前修復警告。

## 測試指引
- 框架：`pytest`；`tests/` 與 `src/` 對應（如 `tests/module/test_feature.py`）。
- 測試檔命名為 `test_*\.py`；善用 fixtures 與參數化。
- 變更程式碼目標涵蓋率 ≥ 90%：`pytest --cov=src --cov-report=term-missing`。

## 提交與 Pull Request 準則
- 提交訊息：祈使句、精簡主旨（≤ 72 字元），正文說明原因。
  - 範例：`fix(parser): handle empty input in tokenizer`
- PR：清楚描述、連結議題（`Closes #123`）、提供測試步驟；行為或 UI 變更附截圖／日誌；標示破壞性變更。

## 安全與設定提示
- 不要提交祕密金鑰。使用 `.env`（由 `.gitignore` 排除），以 `os.getenv` 讀取。
- 鎖定正式相依；透過 `pip-compile` 或受控版本更新。
- 驗證輸入；安全處理檔案（避免不受信任的 eval/exec）。

## 代理（Agent）專用說明
- 本文件適用於此儲存庫所有檔案的協作規範。
- 變更應最小化並符合既有模式；行為變更請補齊文件。
- 回覆語言：預設請使用「正體中文」回答；若需求明確指定其他語言，則依指示調整。
