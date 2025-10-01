from datetime import datetime

from flask import Flask, render_template


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def home():
        programs = [
            {
                "name": "智慧製造系",
                "description": "結合機械、電子與自動化，培育跨域製造人才。",
                "icon": "fa-solid fa-gears",
            },
            {
                "name": "商業與管理系",
                "description": "強調實務操作與創業能力，貼近企業需求。",
                "icon": "fa-solid fa-briefcase",
            },
            {
                "name": "設計與媒體系",
                "description": "透過跨媒體整合訓練，打造創意發想與實作能力。",
                "icon": "fa-solid fa-palette",
            },
            {
                "name": "資訊與工程系",
                "description": "雲端、AI、資安並重，鏈結產業新趨勢。",
                "icon": "fa-solid fa-microchip",
            },
        ]

        news = [
            {
                "date": "2025/10/01",
                "title": "110 週年校慶系列活動開跑",
                "category": "校園活動",
            },
            {
                "date": "2025/09/20",
                "title": "與台北智慧城聯盟簽訂產學合作備忘錄",
                "category": "產學合作",
            },
            {
                "date": "2025/09/10",
                "title": "2025 校園徵才博覽會圓滿落幕",
                "category": "就業職涯",
            },
        ]

        return render_template(
            "index.html",
            programs=programs,
            news=news,
            current_year=datetime.now().year,
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
