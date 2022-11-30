from cProfile import label
import email
from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,ValidationError
from wtforms.validators import Length, EqualTo, DataRequired, Email
from main.models import User


class RegisterForm(FlaskForm):

    def validate_username(self,username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exist')

    def validate_email_address(self,email_address_to_check):
        email_address = User.query.filter_by(email=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email already exist')

    username = StringField(label='User Name: ' , validators=[Length(min=4, max=30), DataRequired()])
    email_address = StringField(label='Email Address: ', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='password: ', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password: ', validators=[EqualTo('password1'), DataRequired()])
    about = StringField(label='About Yourself: ', validators=[DataRequired()])
    submit = SubmitField(label='submit')



class LoginForm(FlaskForm):
    username = StringField(label='username', validators=[DataRequired()])
    password = StringField(label='password', validators=[DataRequired()])
    submit = SubmitField(label='signin')


class ActivitiesForm(FlaskForm):
    activity_name = ''
    activity_date = ''
    activity_desc = ''
    submit = SubmitField(label='Ok')
