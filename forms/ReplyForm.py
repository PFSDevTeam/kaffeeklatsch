from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ReplyForm(FlaskForm):
    
    post = SubmitField('post')
    like = SubmitField('like')
    ownerName = StringField('owner name', default='John Doe')
    communityInfo = StringField('community', default='Community Name')
    userInfo = StringField('user', default='User Info')
    postTitle = StringField('post', default='Post Title')
    ownerContent = StringField('owner', default='All of the news..')
    replyContent = StringField('reply', default='Reply Content')
    upArrow = SubmitField('↑')
    downArrow = SubmitField('↓')