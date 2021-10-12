# Imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField

# Define the elements of the CommunityPainForm
class CommunityPainForm(FlaskForm):
    join = SubmitField('join +')