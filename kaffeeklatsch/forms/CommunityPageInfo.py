#File: CommunityPageInfo.py
#@author: Emily Godwin
#Description: This file contains the logic to handle the community
#    page information for given community

#imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class CommunityPageInfo(FlaskForm):
    communityName = StringField('communityName', default='communityName')
    communityTagline = StringField('communityTagline', default='communityTagline')
    communityContent = StringField('communityContent', default='communityContent')
