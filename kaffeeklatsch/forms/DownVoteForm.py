#File: ChangeContentForm.py
#@author: Geoff Floding, David Hovey
#Description: this file contains the form to grab down arrow
#   submission

# Imports
from flask_wtf import FlaskForm
from wtforms import SubmitField

# Class containing the two objects that link to increment and decrement functions for the post's tally
class DownVoteForm(FlaskForm):
    downArrow = SubmitField('↓')
