#File: CommunityInfoForm.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length


class CommunityInfoForm(FlaskForm):
    communityname = StringField('Enter your Community Name:',
                            validators =[DataRequired(),
                            Length(min=1, max=25)], render_kw={"placeholder": "community name"})
    communitytagline = StringField('Enter your Community Tagline:',
                            validators =[Length(min=1, max=100, message='Your content cannot be longer than 100 characters!') ], render_kw={"placeholder": "community tagline"})
    communitycontent = TextAreaField('Enter your Community Content:', validators =[Length(min=1, max=500, message='Your content cannot be longer than 500 characters!')], render_kw={"placeholder": "community content"})
    communityavatar = SelectField('Enter your Avatar Selection:', choices=[('bee_avatar.png', 'bee'), ('beaver_avatar.png', 'beaver'),
                                    ('elephant_avatar.png', 'elephant'), ('frog_avatar.png', 'frog'),
                                    ('giraffe_avatar.png', 'giraffe'), ('koala_avatar.png', 'koala'),
                                    ('lion_avatar.png', 'lion'), ('macaw_avatar.png', 'macaw'),
                                    ('owl_avatar.png', 'owl'), ('penguin_avatar.png', 'penguin'),
                                    ('spider_avatar.png', 'spider'), ('whale_avatar.png', 'whale')])
    #submit field to update user avatar
    submit = SubmitField('submit')
    