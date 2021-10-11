# Imports necessary for the form to function
from flask_wtf import FlaskForm
from wtforms import SubmitField

# Class containing the two objects that link to increment and decrement functions for the post's tally
class VoteForm(FlaskForm):
    upArrow = SubmitField('↑')
    downArrow = SubmitField('↓')