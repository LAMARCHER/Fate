# coding:utf-8
from flask import current_app, render_template, request, redirect, session, url_for
from flask_sqlalchemy import abort

from . import main
from Manage import app
from app.main.forms import IndexSearchForm
from app.Model import Fate


@main.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)

    pagination = Fate.query.order_by(Fate.create_time.desc()).paginate(
            page, per_page=current_app.config['FATE_PER_PAGE'], error_out=False)

    goods = pagination.items
    form = IndexSearchForm()
    if form.validate_on_submit():
        print('??')
        search = form.search.data
        session['search'] = search
        return redirect(url_for('main.filtedData'))
    return render_template('newIndex.html', goods=goods, pagination=pagination, form=form)


@main.route('/filter/', methods=['GET', 'POST'])
def filtedData():
    search = session.get('search')
    form = IndexSearchForm()
    page = request.args.get('page', 1, type=int)
    if form.validate_on_submit():
        search = form.search.data
        session['search'] = search
    search = '%' + search + '%'
    pagination = Fate.query.order_by(Fate.create_time.desc()).filter(Fate.good_name.ilike(search)).paginate(
        page, per_page=current_app.config['FATE_PER_PAGE'], error_out=False
    )
    form.search.data = search.strip('%')
    goods = pagination.items
    return render_template('filtedData.html', goods=goods, pagination=pagination, form=form)