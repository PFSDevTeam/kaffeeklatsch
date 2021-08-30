#David Hovey Test Forms class week 7
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length 

class HateListRegistrationForm(FlaskForm):
   firstName = StringField('First Name', 
                           validators=[DataRequired(),
                           Length(min=1, max=25)])
   lastName = StringField('Last Name', 
                           validators=[DataRequired(),
                           Length(min=1, max=25)])
   reasonForHate = StringField('Reason I Hate You', validators=[DataRequired()])

   #submit button
   submit = SubmitField('registerHate')

    
    
    