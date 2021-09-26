from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class MakePostForm(FlaskForm):
    postTitle = StringField('post title', default='post title')
    postContent = StringField('post content', default='Start your Discourse...')
    post = SubmitField('post')