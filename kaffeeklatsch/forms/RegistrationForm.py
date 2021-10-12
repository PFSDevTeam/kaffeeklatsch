
#File: RegistrationForm.py
#@author: Ryan Dombek, Geoff Floding, David Hovey
#Description: this file contains the form to register the user
#   based on given credentials

# Imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo


# Define the elements of the RegistrationForm
class RegistrationForm(FlaskForm):
    username = StringField('username',
                            validators =[DataRequired(),
                            Length(min=1, max=25)])
    # Regex pattern taken from https://www.section.io/engineering-education/password-strength-checker-javascript/
    password = PasswordField('password',
                            validators = [DataRequired(),
                            Length(min=8, max=64, message='Password length must be between 8 and 64 characters.'),
                            Regexp('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{8,64})', message="Password must contain 1 lower and upper case letter, number and a special character")])
    repeatPassword = PasswordField('Repeat Password', validators = [EqualTo('password', message='Passwords must match')])
    submit = SubmitField('submit')
