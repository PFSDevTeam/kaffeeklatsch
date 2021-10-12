# Imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length

# Define the elements of the ChangeTaglineForm
class ChangeTaglineForm(FlaskForm):
    #validation for tagline, requirement: length must be 0-20 characters
    taglineChange = StringField('change your tagline:', validators =[Length(min=1, max=50, message='Your tagline cannot be longer than 50 characters!')], render_kw={"placeholder": "new Tagline"})
    submit = SubmitField('update tagline')