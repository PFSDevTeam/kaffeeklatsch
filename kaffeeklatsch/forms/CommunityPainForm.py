#File: CommunityPainForm.py
#@author: Ryan Dombek, Geoff Floding, David Hovey
#Description: this file contains the form to submit
#   from the community pane in feed

# Imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField

# Define the elements of the CommunityPainForm
class CommunityPainForm(FlaskForm):
    join = SubmitField('join +')
