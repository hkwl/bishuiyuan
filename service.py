# encoding=utf-8
import sys

from flask import Flask,render_template

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
from controller import system
system.route(app)

# 数据库配置配置文件路径
#uban.config["DB_CONFIG_FILE"] = os.path.join(os.path.split(os.path.realpath(__file__))[0], "db.ini")
@app.route('/')
def hello_world():
    return render_template('templates/base.html')

if __name__ == '__main__':
    app.run(host='123.56.201.7',port=50003)
