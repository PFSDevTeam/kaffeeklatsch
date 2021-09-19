from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class PostForm(FlaskForm):
    x = 'post content'
    postContent = StringField(x)
    post = SubmitField('post')
    