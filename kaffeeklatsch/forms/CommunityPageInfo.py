#File: CommunityPageInfo.py
#@author: Emily Godwin
#Description: This file contains the logic to handle the profile
#    page information for the current user

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class CommunityPageInfo(FlaskForm):
    communityName = StringField('communityName', default='communityName')
    communityTagline = StringField('communityTagline', default='communityTagline')
    communityContent = StringField('communityContent', default='communityContent')