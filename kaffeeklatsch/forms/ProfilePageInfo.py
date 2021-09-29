#File: ProfilePageInfo
#@author: Emily Godwin
#Description: This file contains the logic to handle the profile
#    page information for the current user

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ProfilePageInfo(FlaskForm):
    userName = StringField('userName', default='username')
    tagline = StringField('tagline', default='user tagline')
    dateJoined = StringField('dateJoined', default='1/1/2021')
    userContent = StringField('user content', default='Spill the Beans...')