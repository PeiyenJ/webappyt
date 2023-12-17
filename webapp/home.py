from flask import Blueprint, render_template, request, send_file
from pytube import YouTube
from .models import Video
from . import db

home = Blueprint('home',__name__)

# API，預設GET，因此需要增加list存放兩種method->methods
@home.route('/',methods=["GET","POST"])

def download_youtube_video():
        
        if request.method =="POST":
                # 把用戶在前端的存在form的網址取出
                video_url = request.form.get("downloadUrl")

                # 用取出來的網址 創造物件
                youtube_video_object = YouTube(video_url, use_oauth=True)

                # 用model裡面的功能 取得影片的觀看數、作者還有影片名稱
                views = youtube_video_object.views
                author = youtube_video_object.author
                video_title = youtube_video_object.title

                # 寫入資料庫,import video, import db
                new_video = Video(views, author, video_title)
                db.session.add(new_video)
                db.session.commit()

                # 下載影片到伺服器
                get_video = youtube_video_object.streams.get_highest_resolution()
                
                # 下載存放， attachment 是附件
                return send_file(get_video.download(), as_attachment=True)

        # 如果不是POST 就是GET
        else:
                # 讀取資料庫,query查詢 all全部
                videos = Video.query.all()
                # 把讀取出來的資料送到前端呈現
                return render_template("home.html", videos=videos)

                # 最後回html設定變數
