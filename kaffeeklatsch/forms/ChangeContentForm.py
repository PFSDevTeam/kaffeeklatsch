#File: ChangeContentForm.py
#@author: Emily Godwin
#Description: this file contains the form to update the user's content
#   as called by the change_content.html form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length


class ChangeContentForm(FlaskForm):
    #validation for tagline, requirement: length must be 0-20 characters
    newContent = StringField('change your content:', validators =[Length(min=0, max=500, message='Your content cannot be longer than 500 characters!')], render_kw={"placeholder": "new user content"})
    submit = SubmitField('update content')