# coding:utf-8
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_EKY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = '[FLASKY]'
    FLASK_MAIL_SENDER = '13598508974@126.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASK_POSTS_PER_PAGE = 10
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'smtp.139.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USER_NAME = '13598508974'
    MAIL_PASSWORD = 'LIU1028140200'
    FATE_PER_PAGE = 30


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/spider?charset=utf8'


config = {
    'dev': DevConfig,
    'default': DevConfig,

}