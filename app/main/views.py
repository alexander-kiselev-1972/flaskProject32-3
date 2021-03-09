from flask import render_template, redirect, url_for, flash
from . import main

from ..models import User, Menu
from app import db
from .forms import NameForm, Menu_create



@main.route('/menu', methods=['GET', 'POST'])

def menu_create():
    form = Menu_create()
    if form.validate_on_submit():
        name = Menu.query.filter_by(name=form.name.data).first()
        if name is None:
            name_menu = Menu(name=form.name.data, url=form.url.data)
            db.session.add(name_menu)
            db.session.commit()
            flash('Новый объект меню создан')
            form.name.data = ''
            return redirect(url_for('main.menu_create'))
    menu = Menu.query.all()
    return render_template('menu.html', menu=menu, form=form)


@main.route('/', methods=['GET', 'POST'])
def index():
    menu = Menu.query.all()

    form = NameForm()
    if form.validate_on_submit():

        name = User.query.filter_by(name=form.name.data).first()
        if name is None:
            user = User(name=form.name.data)
            db.session.add(user)
            db.session.commit()
            flash('Записали новенького')
            form.name.data = ''
            return redirect(url_for('main.index'))
    users = User.query.all()

    return render_template('caravan/index.html', form=form, user=users,
                           menu=menu,
                           source="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js")

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@main.route('/menu#part1')
def part1():
    return render_template('index.html/#part1')