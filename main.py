# 從 flask 套件中匯入 Flask 類別，用來建立一個 Flask 應用程式實例。
from flask import Flask

# 從 flask 套件中匯入 Flask 類別，用來建立一個 Flask 應用程式實例。
# __name__ 是 Python 內建變數，代表目前模組的名稱。Flask 會用它來決定靜態檔案和範本 (templates) 的路徑。
app=Flask(__name__)

# 當使用者造訪根路徑，執行下面這個函式
@app.route("/")
def initMain():
    return "Hello from class-practise-web!"

# 當使用者造訪根路徑，執行下面這個函式
@app.route("/name")
def initName():
    return "<h1 style='{'color':'red'}'>Hello from name!</h1>"

# 只有當這個檔案被直接執行（python main.py）時，才啟動 Flask 伺服器
if __name__ == "__main__":
        app.run(debug=True)

