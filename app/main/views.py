from flask import render_template, redirect, url_for, flash, request
from . import main
from ..email import send_email, send_email2
from ..models import User, Menu, Owner
from app import db
from .forms import NameForm, Menu_create, LeaveMessage
import json



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
    #menu = Menu.query.all()
    own = Owner.query.all()
    form = LeaveMessage()
    #form = NameForm()
    if request.method == 'POST':

        if form.validate_on_submit():

            user = User(first_name=form.first_name.data,
                      last_name=form.last_name.data,
                     email=form.email.data,
                     subject=form.subject.data,
                     message=form.message.data)
            email = User.query.filter_by(email=form.email.data).first()
            if email is None:

                try:
                    db.session.add(user)
                    db.session.commit()

                except:
                   pass

            send_email('deilmann.sro@gmail.com', 'Confirm Your Account',
                    'mail/new_user', user=user)
            return json.dumps({'success': 'true', 'msg': 'Your message sent successfully'})

        else:
            return json.dumps({'success': 'false', 'msg': 'Check our fields please'})

    return render_template('caravan/index.html',  own=own,
                            form=form)


@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@main.route('/menu#part1')
def part1():
    return render_template('index.html/#part1')