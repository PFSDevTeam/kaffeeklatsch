from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField

class MakePostForm(FlaskForm):
    postTitle = StringField('post title', validators=[DataRequired(), Length(min=1, max=50)], render_kw={"placeholder": "post title"})
    postContent = StringField('post content', validators=[DataRequired(), Length(min=1, max=250)], render_kw={"placeholder": "Start your Discourse..."})
    post = SubmitField('post')