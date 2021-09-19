from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField

community = 'Community Name'
class ReplyForm(FlaskForm):
    ownerContent = TextAreaField('Owner Name')
    post = SubmitField('post')
    communityInfo = TextAreaField(community)
    userInfo = TextAreaField('User Info')
    postTitle = TextAreaField('Post Title')
    replyContent = StringField('Reply Content')
    