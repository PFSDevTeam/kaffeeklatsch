#File: CommunityInfoForm.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class CommunityInfoForm(FlaskForm):
    communityname = StringField('communityname',
                            validators =[DataRequired(),
                            Length(min=1, max=25)], render_kw={"placeholder": "enter community name"})
    communitytagline = StringField('communitytagline',
                            validators =[Length(min=1, max=50)], render_kw={"placeholder": "enter community tagline"})
    communitycontent = StringField('communitycontent', validators =[Length(min=1, max=50)], render_kw={"placeholder": "enter community content"})
    communityavatar = SelectField('avatarChoice', choices=[('bee_avatar.png', 'bee'), ('beaver_avatar.png', 'beaver'),
                                    ('elephant_avatar.png', 'elephant'), ('frog_avatar.png', 'frog'),
                                    ('giraffe_avatar.png', 'giraffe'), ('koala_avatar.png', 'koala'),
                                    ('lion_avatar.png', 'lion'), ('macaw_avatar.png', 'macaw'),
                                    ('owl_avatar.png', 'owl'), ('penguin_avatar.png', 'penguin'),
                                    ('spider_avatar.png', 'spider'), ('whale_avatar.png', 'whale')])
    #submit field to update user avatar
    submit = SubmitField('submit')
    