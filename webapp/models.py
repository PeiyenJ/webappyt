# 置入db 物件
from . import db

# 定義資料庫的model
class Video(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  views = db.Column(db.Integer)
  author = db.Column(db.String(255))
  video_title = db.Column(db.String(255))

  # Video物件的初始(self 自行+三個參數)
  def __init__(self, views, author, video_title):
    # 用self. 來區別這個models檔案裡面的變量跟__init__裡面的參數
    # 這邊的self.views就是第7行的views
    self.views = views  # views是 7 = 12行的參數名字
    self.author = author # author 是 8 = 12
    self.video_title = video_title # video_title 9 = 12