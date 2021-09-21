from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class PostForm(FlaskForm):
    x = 'Sort Posts By:'
    postContent = StringField('sort', default='Sort Posts By: ')
    popularity = SubmitField('popularity')
    recent = SubmitField('recent')
    bean = SubmitField('bean')
