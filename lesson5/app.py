# WenTest
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # 課程資訊
    course_info = {
        "title": "Python 機器學習實戰課程",
        "subtitle": "從零開始掌握 AI 技術",
        "duration": "12 週",
        "level": "初級到中級",
        "price": "NT$ 15,000",
        "instructor": "王大明 博士",
        "start_date": "2025 年 11 月 1 日",
    }

    # 課程特色
    features = [
        {
            "icon": "📚",
            "title": "完整教材",
            "description": "提供完整的課程講義與實作範例程式碼",
        },
        {
            "icon": "💻",
            "title": "實作導向",
            "description": "每週實作專案，從做中學習機器學習技術",
        },
        {
            "icon": "👨‍🏫",
            "title": "專業師資",
            "description": "業界資深 AI 工程師親自授課與輔導",
        },
        {
            "icon": "🎓",
            "title": "結業證書",
            "description": "完成課程可獲得職能發展學院認證證書",
        },
    ]

    # 課程大綱
    curriculum = [
        {"week": 1, "topic": "Python 基礎與環境設置", "content": "Python 語法、Jupyter Notebook"},
        {"week": 2, "topic": "NumPy 與資料處理", "content": "陣列運算、資料清理"},
        {"week": 3, "topic": "Pandas 資料分析", "content": "DataFrame 操作、資料視覺化"},
        {"week": 4, "topic": "機器學習入門", "content": "監督式學習、非監督式學習"},
        {"week": 5, "topic": "Scikit-learn 實作", "content": "分類問題、迴歸分析"},
        {"week": 6, "topic": "深度學習基礎", "content": "神經網路、TensorFlow"},
        {"week": 7, "topic": "影像辨識專案", "content": "CNN、影像分類"},
        {"week": 8, "topic": "自然語言處理", "content": "文字處理、情感分析"},
        {"week": 9, "topic": "模型優化與調參", "content": "超參數調整、交叉驗證"},
        {"week": 10, "topic": "專案實作（一）", "content": "選定題目開始實作"},
        {"week": 11, "topic": "專案實作（二）", "content": "完善模型與部署"},
        {"week": 12, "topic": "成果發表", "content": "專案展示與經驗分享"},
    ]

    # 學員評價
    reviews = [
        {
            "name": "李小華",
            "rating": 5,
            "comment": "課程內容紮實，老師講解清楚，很適合初學者入門！",
            "date": "2025-09-15",
        },
        {
            "name": "張志明",
            "rating": 5,
            "comment": "實作專案很有挑戰性，學到很多實用的技巧。",
            "date": "2025-09-10",
        },
        {
            "name": "陳美玲",
            "rating": 4,
            "comment": "整體課程很棒，建議可以增加更多實際案例分享。",
            "date": "2025-09-05",
        },
    ]

    # FAQ
    faqs = [
        {"question": "需要有程式基礎嗎？", "answer": "建議有基礎 Python 語法概念，但課程會從基礎開始教學。"},
        {"question": "上課方式是線上還是實體？", "answer": "採線上直播授課，課後提供錄影回放，可彈性安排學習時間。"},
        {"question": "是否提供課後輔導？", "answer": "提供專屬 Discord 頻道，講師與助教會協助解答問題。"},
        {"question": "完成課程後能獲得什麼？", "answer": "可獲得結業證書，以及完整的專案作品集。"},
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
    """啟動應用（教學用：啟用 debug 模式）"""
    # 在開發環境下使用 debug=True，部署時請關閉
    app.run(debug=True)

if __name__ == "__main__":
    main()