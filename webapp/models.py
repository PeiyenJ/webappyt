# 置入需要用到的工具
from . import db


# 定義資料庫的物件
class Video(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  views = db.Column(db.Integer)
  author = db.Column(db.String(255))
  video_title = db.Column(db.String(255))

  # 定義Video物件的初始值
  def __init__(self, views, author, video_title):
    # 資料庫會自動產生新的id，所以不用我們給初始值
    # 這邊的self.views就是第7行的views
    # 用self. 來區別這個models檔案裡面的變量跟__init__裡面的參數
    self.views = views  # views是第12行的參數名字
    self.author = author
    self.video_title = video_title