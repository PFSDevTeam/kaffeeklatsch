from datetime import datetime
from kaffeeklatsch import db

class UserAccess(db.Model):
    username = db.Column(db.Text, nullable=False, unique=True, primary_key=True)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"User Access Profile:('{self.username}', '{self.password}')"

class User(db.Model):
    username = db.Column(db.Text, db.ForeignKey('user_access.username'), nullable=False, primary_key=True)
    avatar = db.Column(db.Text, nullable=True)
    first_name = db.Column(db.Text, nullable=True)
    last_name = db.Column(db.Text, nullable=True)
    communities = db.Column(db.Text, nullable=True)
    users_following = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"User Profile: ('{self.username}')"