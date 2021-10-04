from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField

class MakePostForm(FlaskForm):
    postTitle = StringField('post title', default='post title', validators=[DataRequired(), Length(min=1, max=50)])
    postContent = StringField('post content', default='Start your Discourse...', validators=[DataRequired(), Length(min=1, max=250)])
    post = SubmitField('post')