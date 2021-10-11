from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Regexp


class ChangePasswordForm(FlaskForm):
    #validation for newPassword, requirement: must be 8-64 characters, contain 1 upper and lower case letter, one number and one special character
    newPassword = PasswordField('change your password:',
                                validators = [Length(min=8, max=64, message='Password length must be between 8 and 64 characters.'),
                                Regexp('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{8,64})', message="Password must contain 1 lower and upper case letter, number and a special character")], render_kw={"placeholder": "new Password"})
    verifyPassword = PasswordField('verify new password:', validators = [EqualTo('newPassword', message='Passwords must match')], render_kw={"placeholder": "verify Password"})
    submit = SubmitField('change password')