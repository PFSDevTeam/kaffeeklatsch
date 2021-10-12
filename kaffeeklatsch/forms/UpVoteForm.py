#File: UpVoteForm.py
#@author: Geoff Floding
#Description: this file contains the form to
#   grab SubmitField input on the vote panel

# Imports necessary for the form to function
from flask_wtf import FlaskForm
from wtforms import SubmitField

# Class containing the two objects that link to increment and decrement functions for the post's tally
class UpVoteForm(FlaskForm):
    upArrow = SubmitField('↑')
