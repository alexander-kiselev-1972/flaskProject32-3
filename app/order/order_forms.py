from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, RadioField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Email, Length, Regexp, ValidationError
from ..models import User, Mattress
from flask import current_app



def get_data_models(table):
    if current_app:
        list_table = []
        data = table.query.all()
        for i in data:
            tuple_data = (i.id, i.name)
            list_table.append(tuple_data)
        return list_table




class CheckoutForm(FlaskForm):
    csrf_token = HiddenField()
    heater = SelectField('Heater', choices=get_data_models(Mattress))
    mattress = SelectField('Mattress', choices=get_data_models(Mattress))
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
    email = StringField('Your e-mail', validators=[DataRequired(), Regexp(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"), Email()])
    phone = StringField('Your phone')
    billing_address = StringField('Your address', validators=[DataRequired()])
    type_of_document = StringField('Which document', validators=[DataRequired()])
    document = StringField('Number of your document', validators=[DataRequired()])
    submit = SubmitField('Купить')
