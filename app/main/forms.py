from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, Form, validators
from wtforms.validators import DataRequired, Email, Length, Regexp
from ..models import User
from wtforms import ValidationError



class NameForm(FlaskForm):
    name = StringField('Name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class Menu_create(FlaskForm):
    name = StringField('Name?', validators=[DataRequired()])
    url = StringField("URL", validators=[DataRequired()])
    submit = SubmitField('Submit')


class LeaveMessage(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Regexp(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')



