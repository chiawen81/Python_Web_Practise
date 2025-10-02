from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    course_info = {
        "title": "Python 機器學習實戰課程",
        "subtitle": "從零開始掌握 AI 關鍵技能",
        "duration": "12 週",
        "level": "初階到中階",
        "price": "NT$ 15,000",
        "instructor": "林大偉博士",
        "start_date": "2025 年 11 月 1 日",
    }

    features = [
        {
            "icon": "🧭",
            "title": "完整學習路線",
            "description": "從基礎語法到實際專案，循序漸進掌握核心技能。",
        },
        {
            "icon": "🛠️",
            "title": "實戰導向",
            "description": "每週親自動手做，透過專案練習深化理解。",
        },
        {
            "icon": "👨‍🏫",
            "title": "專業師資",
            "description": "資深 AI 工程師授課，提供實務經驗與指導。",
        },
        {
            "icon": "🎓",
            "title": "結業證書",
            "description": "修畢課程後獲得證書，強化履歷與職涯競爭力。",
        },
    ]

    curriculum = [
        {"week": 1, "topic": "Python 與開發環境設定", "content": "Python 語法基礎、Jupyter Notebook"},
        {"week": 2, "topic": "NumPy 與矩陣運算", "content": "陣列操作、線性代數入門"},
        {"week": 3, "topic": "Pandas 資料處理", "content": "DataFrame 清理、資料視覺化"},
        {"week": 4, "topic": "機器學習概念", "content": "監督式與非監督式學習"},
        {"week": 5, "topic": "Scikit-learn 實作", "content": "分類、迴歸與模型評估"},
        {"week": 6, "topic": "深度學習基礎", "content": "神經網路與 TensorFlow"},
        {"week": 7, "topic": "影像辨識專題", "content": "卷積神經網路與影像資料"},
        {"week": 8, "topic": "自然語言處理", "content": "文字向量化與情感分析"},
        {"week": 9, "topic": "模型優化與調參", "content": "超參數調整、交叉驗證"},
        {"week": 10, "topic": "專題實作（一）", "content": "題目選定與資料蒐集"},
        {"week": 11, "topic": "專題實作（二）", "content": "模型精進與成果整合"},
        {"week": 12, "topic": "成果發表日", "content": "專題展示與經驗分享"},
    ]

    reviews = [
        {
            "name": "王小明",
            "rating": 5,
            "comment": "課程內容紮實，老師講解清楚，讓我快速進入 AI 世界。",
            "date": "2025-09-15",
        },
        {
            "name": "張雅筑",
            "rating": 5,
            "comment": "實作專題很有挑戰，也學到很多實用技巧。",
            "date": "2025-09-10",
        },
        {
            "name": "李俊豪",
            "rating": 4,
            "comment": "課程很充實，建議可以加入更多產業案例分享。",
            "date": "2025-09-05",
        },
    ]

    faqs = [
        {
            "question": "需要具備程式基礎嗎？",
            "answer": "建議具備基本 Python 概念，課程會由淺入深引導學習。",
        },
        {
            "question": "上課方式是線上還是實體？",
            "answer": "以線上直播為主，課後提供錄影回放，方便複習。",
        },
        {
            "question": "是否提供課後輔導？",
            "answer": "設有專屬 Discord 社群，助教與講師提供即時協助。",
        },
        {
            "question": "完課後能獲得什麼？",
            "answer": "取得結業證書與完整專案作品，強化履歷競爭力。",
        },
    ]

    return render_template(
        "index.html",
        course_info=course_info,
        features=features,
        curriculum=curriculum,
        reviews=reviews,
        faqs=faqs,
    )


def main():
    """啟動開發用伺服器（教學用：保留 debug 模式）"""
    print("test")
    app.run(debug=True)


if __name__ == "__main__":
    main()
