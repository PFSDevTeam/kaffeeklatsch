#File: ReplyForm.py
#@author: David Hovey
#Description: this file contains the form to grab
#   the reply fields in the post pane

# Imports
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField

# Define the elements of the ReplyForm
class ReplyForm(FlaskForm):
    post = SubmitField('post')
    join = SubmitField('join +')
    replyContent = StringField('reply', validators=[DataRequired(), Length(min=1, max=250)], render_kw={"placeholder": "Reply to Post"})
    
