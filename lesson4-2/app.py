from flask import Flask

app=Flask(__name__,static_folder="static",template_folder="templates")


# 當使用者造訪根路徑，執行下面這個函式
@app.route("/")
def initMain():
    return "Hello World, from class-practise-web!"

# 當使用者造訪根路徑，執行下面這個函式
@app.route("/name")
def initName():
    return "<h1>Hello from name!</h1>"

# 只有當這個檔案被直接執行（python main.py）時，才啟動 Flask 伺服器
if __name__ == "__main__":
        app.run(debug=True)