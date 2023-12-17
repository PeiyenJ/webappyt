from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 創造SQLAlchemy (object)
db = SQLAlchemy()

# 一個variable去存放資料庫的名稱
YOUTUBE_DATABASE = "youtube_database.db"

def create_web_app():
        # 創建一個flask物件 叫做app

        app = Flask(__name__)

        # 設置資料庫連結
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{YOUTUBE_DATABASE}'
        # 初始化資料庫
        db.init_app(app)

        # 註冊藍圖.引入home模組
        from .home import home
        app.register_blueprint(home, url_prefix='/')

        # 創建資料庫,建立model
        with app.app_context():
                db.create_all()

        # 當create_web_app在別的地方被呼叫的時後，返迴app物件給呼叫方
        return app
