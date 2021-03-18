from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin
from . import db, login_manager



class Owner(db.Model):
    __tablename__='own'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, default='Deilmann s.r.o.')
    email1 = db.Column(db.String(128), default='karavan@deilmann.sk')
    email2 = db.Column(db.String(128))
    email3 = db.Column(db.String(128))
    phone1 = db.Column(db.String(12), unique=True, default='+421-950-764-554')
    phone2 = db.Column(db.String(12), unique=True)
    phone3 = db.Column(db.String(12), unique=True)
    icho = db.Column(db.Integer, unique=True)
    ulica_dom = db.Column(db.String(128))
    index = db.Column(db.Integer)

    def getOwn(self):
        own = Owner.query.all()


    def setOwn(self, name, email1, email2='', email3=''):
        own = Owner(name=name, email1=email1, email2=email2,email3=email3)
        db.session.add(own)
        db.session.commit()


    def __repr__(self):
        return self.name


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    subject = db.Column(db.String(128))
    message = db.Column(db.Text)



    def user_insert(self, name):
        user = User(name=name)
        db.session.add(user)
        db.session.commit()

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            return True

    def __repr__(self):
        return self.first_name


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(128), unique=True)

    def __repr__(self):
        return self.role


class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16


class Menu(db.Model):
    __tablename__='menu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    url = db.Column(db.String(128), unique=True)

    def set_menu(self, name, url):
        name_menu = Menu(name=name, url=url)
        db.session.add(name_menu)
        db.session.commit()


    def __repr__(self):
        return self.name