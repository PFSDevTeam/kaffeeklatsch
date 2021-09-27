from datetime import datetime
from kaffeeklatsch import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)

class UserAccess(db.Model):
    username = db.Column(db.Text, nullable=False, unique=True, primary_key=True)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"User Access Profile:('{self.username}', '{self.password}')"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    username = db.Column(db.Text, db.ForeignKey('user_access.username'), nullable=False)
    avatar = db.Column(db.Text, nullable=True)
    first_name = db.Column(db.Text, nullable=True)
    last_name = db.Column(db.Text, nullable=True)
    communities = db.Column(db.Text, nullable=True)
    users_following = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"User Profile: ('{self.username}')"

class Community(db.Model):
    community = db.Column(db.Text, nullable=False, primary_key=True)

    def __repr__(self):
        return f"community: ('{self.community}')"

class Post(db.Model):
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    posting_user = db.Column(db.Text, db.ForeignKey('user_access.username'), nullable=False)
    posted_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    community = db.Column(db.Text, nullable=False)
    UUID = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)

    def __repr__(self):
        return f"""\nPost {self.UUID}:
        \n\t-author: {self.posting_user}
        \n\t-posted_date: {self.posted_date}
        \n\t-community: {self.community}
        \n\t-content: {self.content}
        \n"""

