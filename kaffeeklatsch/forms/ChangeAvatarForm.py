from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class ChangeAvatarForm(FlaskForm):
    # avatar change
    # newAvatar = StringField('change your Avatar',  render_kw={"placeholder": "enter the name of the avatar"})
    newAvatar = SelectField('avatarChoice', choices=[('bee_avatar.png', 'bee'), ('beaver_avatar.png', 'beaver')])
    submit = SubmitField('update avatar')