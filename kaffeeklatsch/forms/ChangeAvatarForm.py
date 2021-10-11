#File: ChangeAvatarForm.py
#@author: David Hovey, Emily Godwin
#Description: this file contains the form to receive the avatar change form
#       data given by the change_avatar.html template
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class ChangeAvatarForm(FlaskForm):
    # avatar change form field, a select field with the list of avatars
    newAvatar = SelectField('avatarChoice', choices=[('bee_avatar.png', 'bee'), ('beaver_avatar.png', 'beaver'),
                                    ('elephant_avatar.png', 'elephant'), ('frog_avatar.png', 'frog'),
                                    ('giraffe_avatar.png', 'giraffe'), ('koala_avatar.png', 'koala'),
                                    ('lion_avatar.png', 'lion'), ('macaw_avatar.png', 'macaw'),
                                    ('owl_avatar.png', 'owl'), ('penguin_avatar.png', 'penguin'),
                                    ('spider_avatar.png', 'spider'), ('whale_avatar.png', 'whale')])
    #submit field to update user avatar
    submit = SubmitField('update avatar')