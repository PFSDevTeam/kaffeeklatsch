from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SortPostForm(FlaskForm):
    popularity = SubmitField('popularity')
    recent = SubmitField('recent')
    bean = SubmitField('bean')
