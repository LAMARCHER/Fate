# coding:utf-8
from datetime import datetime

from app import db


class Fate(db.Model):
    __tablename__ = 'fate_mh_goods'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    good_name = db.Column(db.String(255))
    good_url = db.Column(db.String(255))
    good_price = db.Column(db.Float(12, 3))
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime)
    good_id = db.Column(db.String(64), unique=True)
    source = db.Column(db.String(32), default='')


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(64), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime)


