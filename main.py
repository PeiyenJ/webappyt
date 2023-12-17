# 客製模組webapp 置入create_web_app的功能
from webapp import create_web_app

# 呼叫create_web_app的功能
app = create_web_app()
# 利用Flask app裡面的功能run來架設網路伺服器
app.run(host='0.0.0.0', port=8080)