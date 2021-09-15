from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('username',
                            validators =[DataRequired(),
                            Length(min=1, max=25)])
    # Regex pattern taken from https://www.section.io/engineering-education/password-strength-checker-javascript/
    password = PasswordField('password', 
                            validators = [DataRequired(),
                            Length(min=8, max=64)],
                            EqualTo('confirm', message='Passwords must match'),
                            Regexp('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{8,64})', message="Password must contain 1 lower and upper case letter, number and a special character") )
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('login')
    