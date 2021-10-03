from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField

class MakePostForm(FlaskForm):
    postTitle = StringField('postTitle')
    postContent = StringField('post-content')
    post = SubmitField('post')