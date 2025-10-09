from flask import Flask, render_template

app = Flask(__name__)


@app.route("/lesson5/hw")
def index():
    school_info = {
        "name": "台北職能學院",
        "slogan": "專業技能，成就未來",
        "address": "台北市大安區復興南路一段390號",
        "phone": "(02) 2733-8221",
    }

    departments = [
        {
            "name": "資訊與通訊",
            "icon": "💻",
            "description": "學習最新的軟體開發、網路管理與資安技術。",
            "courses": ["Python 網站開發", "Java 企業級應用", "網路工程師養成"],
        },
        {
            "name": "創意設計",
            "icon": "🎨",
            "description": "培養視覺設計、多媒體製作與使用者體驗設計能力。",
            "courses": ["商業視覺設計", "UI/UX 設計實務", "3D 動畫製作"],
        },
        {
            "name": "工商管理",
            "icon": "📈",
            "description": "掌握行銷企劃、人力資源管理與電子商務經營策略。",
            "courses": ["數位行銷策略", "人力資源管理師", "電子商務經營"],
        },
        {
            "name": "觀光餐旅",
            "icon": "✈️",
            "description": "學習觀光導覽、旅館管理與精緻餐飲服務。",
            "courses": ["國際領隊導遊", "旅館管理實務", "西點烘焙創業"],
        },
    ]

    events = [
        {
            "date": "2025-11-15",
            "title": "校園開放日",
            "description": "歡迎參觀我們的教學環境，與講師面對面交流。",
        },
        {
            "date": "2025-12-01",
            "title": "冬季班隊招生說明會",
            "description": "深入了解各科系的課程規劃與未來發展。",
        },
    ]

    return render_template(
        "index.html",
        school_info=school_info,
        departments=departments,
        events=events,
    )


if __name__ == "__main__":
    app.run(debug=True)
