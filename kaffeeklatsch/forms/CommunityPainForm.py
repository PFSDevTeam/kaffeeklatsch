from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField

class CommunityPainForm(FlaskForm):
    join = SubmitField('join +')