from flask import render_template, redirect, url_for, flash, request
from . import main
from ..email import send_email, send_email2
from ..models import User, Menu, Owner, Messages, Models
from app import db
from .forms import NameForm, Menu_create, LeaveMessage
from sqlalchemy.exc import IntegrityError
import json
import time


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


# @main.route('/', methods=['GET', 'POST'])
# def index():
#     #menu = Menu.query.all()
#     #own = Owner.query.all()
#     form = LeaveMessage()
#     #form = NameForm()
#
#     if form.validate_on_submit():
#         user = User(first_name=form.first_name.data,
#                     last_name=form.last_name.data,
#                     email=form.email.data,
#                     subject=form.subject.data,
#                     message=form.message.data)
#         email_user = User.query.filter_by(email=form.email.data).first()
#
#         if email_user == None:
#
#
#             db.session.add(user)
#             db.session.commit()
#             send_email('deilmann.sro@gmail.com', 'Confirm Your Account',                            'mail/new_user', user=user)
#             form.first_name.data = ''
#             form.last_name.data = ''
#             form.email.data = ''
#             form.subject.data = ''
#             form.message.data = ''
#             #return json.dumps({'success': 'true', 'msg': 'Your message sent successfully'})
#
#             # except:
#             #     flash('insert to base not work')
#             return redirect(url_for('main.index'))
#         else:
#             send_email('deilmann.sro@gmail.com', 'Confirm Your Account',
#                         'mail/new_user', user=user)
#             form.first_name.data = ''
#             form.last_name.data = ''
#             form.email.data = ''
#             form.subject.data = ''
#             form.message.data = ''
#
#         return redirect(url_for('main.index'))
#             #return json.dumps({'success': 'true', 'msg': 'Your message2 sent successfully'})
#
#     else:
#         return render_template('caravan/index.html',  form=form)
#
#
# @main.route("/macros")
# def owners_data():
#     owners_data = Owner.query.all()
#     return render_template("caravan/macros.html", own=owners_data)

@main.route('/', methods=['GET', 'POST'])
def index():
    own = Owner.query.all()
    models = Models.query.all()
    form = LeaveMessage()

    if form.validate_on_submit():

        user_email = User.query.filter_by(email=form.email.data).first()
        if user_email is not None:
            flash("пользователь  уже зарегистрирован")
            subject = form.subject.data
            messages = form.message.data
            user_id = User.query.filter_by(email=form.email.data).first().id
            messages_to = Messages(user_id=user_id, subject=subject, message=messages)

            db.session.add(messages_to)
            db.session.commit()

            send_email('deilmann.sro@gmail.com', 'Confirm Your Account',
                   'mail/new_user', user=form.first_name.data, email=form.email.data, user_subject=form.subject.data, user_message=form.message.data )
            flash("your messeges for as send to email")
            form.first_name.data = ''
            form.last_name.data = ''
            form.email.data = ''
            form.subject.data = ''
            form.message.data = ''

            return redirect(url_for('main.index'))

        else:
            flash("новый пользователь")
            user_to = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)

            db.session.add(user_to)
            db.session.commit()

            messages = form.message.data
            subject = form.subject.data
            user_id = User.query.filter_by(email=form.email.data).first().id
            messages_to = Messages(user_id=user_id, subject=subject, message=messages)

            db.session.add(messages_to)
            db.session.commit()

            send_email('deilmann.sro@gmail.com', 'Confirm Your Account',
                       'mail/new_user', user=form.first_name.data, user_subject=form.subject.data, user_message=form.message.data)
            flash("your messeges for as send to email")
            form.first_name.data = ''
            form.last_name.data = ''
            form.email.data = ''
            form.subject.data = ''
            form.message.data = ''
            return redirect(url_for('main.index'))

    return render_template('caravan/index.html', form=form, own=own, models=models)



    # <div class="col-12">{{ form.submit(class="btn anim-btn rounded-pill user-contact", id="submit",  type="submit", value="Submit") }}</div>#}
@main.route("/order", methods=['GET', 'POST'])
def order():
    data_form = request.form
    return render_template('caravan/order.html', data_form=data_form)


@main.route('/cookie')
def cookie():
    return render_template('cookie.html')


#
# @main.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)
#
#
# @main.route('/menu#part1')
# def part1():
#     return render_template('index.html/#part1')