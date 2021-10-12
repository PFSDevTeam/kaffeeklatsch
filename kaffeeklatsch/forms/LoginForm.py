#File: LoginForm.py
#@author: Geoff Floding, David Hovey, Ryan Dombek
#Description: this file contains the form to login
#   a user by grabbing credentials

# Imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

# Define the elements of the LoginForm
class LoginForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    submit = SubmitField('login')
    
