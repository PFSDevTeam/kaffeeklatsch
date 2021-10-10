#File: ProfileSettings.py
#@author: Emily Godwin
#Description: This file contains the logic to handle the profile
#    page information for the current user

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ProfileSettingsForm(FlaskForm):
    taglineChange = StringField('tagline',render_kw={"placeholder": "change tagline"})
    newPassword = StringField('newPassword', render_kw={"placeholder": "new Password"})
    #if(newPassword.length() > 0):
    verifyPassword = StringField('verifyPassword', render_kw={"placeholder": "verify Password"})
    #    avatar
    save = SubmitField('save changes')