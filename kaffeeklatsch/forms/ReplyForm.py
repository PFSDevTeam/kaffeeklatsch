from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ReplyForm(FlaskForm):
    
    post = SubmitField('post')
    join = SubmitField('join +')
    replyContent = StringField('reply', default='Reply Content')
    upArrow = SubmitField('↑')
    downArrow = SubmitField('↓')