from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Email, Length, Regexp, ValidationError
from ..models import User


class NameForm(FlaskForm):
    name = StringField('Name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class CreateMenuForm(FlaskForm):
    name = StringField('Name?', validators=[DataRequired()])
    url = StringField("URL", validators=[DataRequired()])
    submit = SubmitField('Submit')


class LeaveMessageForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(message='Je povinné'), Length(min=2, max=25)])
    last_name = StringField('Last Name', validators=[DataRequired(message='Je povinné'), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email(),
                                             Regexp(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Poslať správu')


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
    submit = SubmitField('Ďalej')


class CheckoutForm(FlaskForm):
    csrf_token = HiddenField()
    heater = BooleanField('Heater')
    hatch_fan = BooleanField('Roof hatch fan')
    caravan_cover = BooleanField('Caravan cover')
    support_legs = BooleanField('Trailer support legs')
    roof_rack = BooleanField('Roof rack cross bars<')
    color = HiddenField('Color')
    chassis = RadioField('Chassis', choices=[('no-chassis', 'Without chassis'), ('with-chassis', 'With chassis')])
    parking_brake = BooleanField('With parking brake')
    spare_tire = BooleanField('Spare tire')
    price = HiddenField()
    model_id = HiddenField()
    first_name = StringField('Your first name', validators=[DataRequired(), Length(min=2, max=25)])
    last_name = StringField('Your last name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Your e-mail', validators=[DataRequired(), Email(),
                                                   Regexp(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")])
    phone = StringField('Your phone')
    billing_address = StringField('Your address', validators=[DataRequired()])
    type_of_document = StringField('Which document', validators=[DataRequired()])
    document = StringField('Number of your document', validators=[DataRequired()])
    submit = SubmitField('Objednať')
