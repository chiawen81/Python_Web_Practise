# Lesson 5 Homework

> 本專案為練習用作業，內容為模仿台北職能學院官網的切版設計，並使用 AI 協助生成部分程式碼與文件。

## 建立虛擬環境
1. 確保已安裝 Python 3.10 或以上版本。
2. 開啟終端機，進入專案目錄：
   ```cmd
   cd lesson5_hw
   ```
3. 建立虛擬環境：
   ```cmd
   python -m venv venv
   ```
4. 啟動虛擬環境：
   - Windows：
     ```cmd
     venv\Scripts\activate
     ```    
   - macOS/Linux：
     ```bash
     source venv/bin/activate
     ```

## 安裝所需套件
1. 確保虛擬環境已啟動。
2. 使用 `pyproject.toml` 安裝套件：
   ```cmd
   pip install .
   ```

## 啟動應用程式
1. 確保虛擬環境已啟動並完成套件安裝。
2. 啟動 Flask 應用程式：
   ```cmd
   python app.py
   ```
3. 開啟瀏覽器並進入以下網址：
   ```
   http://127.0.0.1:5000/lesson5/hw
   ```

## 注意事項
- 若需退出虛擬環境，執行以下指令：
  ```cmd
  deactivate
  ```