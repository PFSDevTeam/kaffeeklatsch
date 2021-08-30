from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('username',
                            validators =[DataRequired(),
                            Length(min=1, max=25)])
    password = PasswordField('password', 
                            validators = [DataRequired(),
                            Length(min=8, max=64)])
    submit = SubmitField('login')
    