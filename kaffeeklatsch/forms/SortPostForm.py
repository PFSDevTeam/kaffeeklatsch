#File: SortPostForm.py
#@author: Ryan Dombek, Geoff Floding, David Hovey
#Description: this file contains the form to take int
#   sorting filters from the sort bar

# Imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# Define the elements of the SortPostForm
class SortPostForm(FlaskForm):
    popularity = SubmitField('popularity')
    recent = SubmitField('recent')
    bean = SubmitField('bean')
