from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Email, Length, Regexp, ValidationError
from ..models import User


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


class BuyCaravanForm(FlaskForm):
    csrf_token = HiddenField()
    heater = BooleanField('Heater')
    hatch_fan = BooleanField('Roof hatch fan')
    caravan_cover = BooleanField('Caravan cover')
    support_legs = BooleanField('Trailer support legs')
    roof_rack = BooleanField('Roof rack cross bars<')
    spare_tire = BooleanField('Spare tire')
    color = HiddenField('Color')
    chassis = RadioField('Chassis', choices=[('no-chassis', 'Without chassis'), ('with-chassis', 'With chassis')])
    parking_brake = BooleanField('With parking brake')
    price = HiddenField()
    model_id = HiddenField()
    submit = SubmitField('Купить')


class CheckoutForm(FlaskForm):
    heater = BooleanField('Heater')
    submit = SubmitField('Заказать')
