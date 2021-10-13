#File: MakePostForm.py
#@author: Ryan Dombek, David Hovey, Geoff Floding
#Description: this file contains the form create a post
#   by taking in post fields

# Imports
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField

# Define the elements of the MakePostForm
class MakePostForm(FlaskForm):
    postTitle = StringField('post title', validators=[DataRequired(), Length(min=1, max=50)], render_kw={"placeholder": "post title"})
    postContent = StringField('post content', validators=[DataRequired(), Length(min=1, max=250)], render_kw={"placeholder": "Start your Discourse..."})
    post = SubmitField('post')
