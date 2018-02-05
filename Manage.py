# coding:utf-8
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from Config import config

app = create_app()
app.config.from_object(config['dev'])#这个放在sqlalchemy初始化前面
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


if __name__ == '__main__':
    app.run(debug=True)
