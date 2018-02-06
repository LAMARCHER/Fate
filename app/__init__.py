# coding:utf-8
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


from Config import config

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(conf='dev'):
    app = Flask(__name__)
    app.config.from_object(config[conf])  # 这个放在sqlalchemy初始化前面
    config[conf].init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app


