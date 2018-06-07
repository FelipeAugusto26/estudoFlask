from flask_wtf import form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(form):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])