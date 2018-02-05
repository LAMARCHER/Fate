# coding:utf-8
from datetime import datetime

from Manage import db


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




