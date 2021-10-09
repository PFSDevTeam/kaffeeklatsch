#File: ProfilePageInfo
#@author: Emily Godwin
#Description: This file contains the logic to handle the profile
#    page information for the current user

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from kaffeeklatsch import db
from kaffeeklatsch.models.models import User

class ProfilePageInfo(FlaskForm):
    username = StringField('userName', default='username')
    tagline = StringField('tagline', default='user tagline')
    date_joined = StringField('dateJoined', default='1/1/2021')
    summary = StringField('user content', default='Spill the Beans...')
    # def getInfo(currUser):
    #     userInfo = User.query.filter_by(username=currUser)
    #     print(userInfo)
    #     return userInfo
    save = SubmitField('save changes')