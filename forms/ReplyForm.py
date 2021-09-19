from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField

class ReplyForm(FlaskForm):
    
    post = SubmitField('Reply')
    ownerName = StringField('John Doe')
    communityInfo = StringField('Community Name')
    userInfo = StringField('User Info')
    postTitle = StringField('Post Title')
    ownerContent = StringField('All of the news..')
    replyContent = StringField('Reply Content')
    upArrow = SubmitField('Amazing')
    downArrow = SubmitField('Mediocre')