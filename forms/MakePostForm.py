from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class MakePostForm(FlaskForm):
    postContent = StringField('post content')
    post = SubmitField('post')