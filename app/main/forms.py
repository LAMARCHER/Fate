# coding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class IndexSearchForm(FlaskForm):
    search = StringField('关键词搜索名称', validators=[DataRequired()])
    submit = SubmitField('Submit')
