# 專案說明
這是一個基於 **Flask (Python)** 的後端專案，使用 **uv** 進行套件與虛擬環境管理。  
主要功能包含 RESTful API、資料處理與模型推論，並規劃與前端 (Vue/React/Angular) 進行整合。  


# 規範
- **專案架構**：遵循 Flask App Factory + Blueprint 模式，避免所有邏輯寫在單一檔案。
- **程式風格**：遵循 PEP8 與 PEP20，命名統一使用 snake_case。
- **環境管理**：使用 `uv` 管理套件，確保相依一致性。
- **資料庫**：使用 SQLAlchemy 作為 ORM，並搭配 Flask-Migrate 做 schema 遷移。
- **測試**：所有主要功能需搭配 pytest 撰寫單元測試，測試檔放在 `tests/`。
- **錯誤處理**：集中管理 Exception Handler，回傳 JSON 格式錯誤訊息。
- **設定**：使用 `config.py` 或 `.env` 管理環境變數 (避免硬編碼)。
- **API 設計**：遵循 RESTful 規範，必要時使用 Marshmallow 進行序列化/驗證。

# 輸出格式
- **程式碼**：盡量完整，可直接執行或貼到對應檔案中即可使用。
- **範例**：以 Flask 標準寫法 (Blueprint + App Factory) 為優先。
- **說明**：請用繁體中文描述用途與注意事項。

# 測試
所有範例程式碼一律要在檔案開頭加上註解： # WenTest
