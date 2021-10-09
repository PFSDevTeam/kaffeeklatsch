#File: ProfileSettings.py
#@author: Emily Godwin
#Description: This file contains the logic to handle the profile
#    page information for the current user

from flask_wtf import FlaskForm
from wtforms import StringField

class ProfileSettings(FlaskForm):
    userName = StringField('userName', default='username')