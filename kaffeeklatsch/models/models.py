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
    tagline = db.Column(db.Text, db.ForeignKey('user_access.tagline'), nullable=True)
    date_joined = db.Column(db.Text, nullable=False)
    avatar = db.Column(db.Text, nullable=True)
    first_name = db.Column(db.Text, nullable=True)
    last_name = db.Column(db.Text, nullable=True)
    communities = db.Column(db.Text, nullable=True)
    users_following = db.Column(db.Text, nullable=True)
    tagline = db.Column(db.Text, nullable=True)
    date_joined = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"User Profile: ('{self.username}')"

class Community(db.Model):
    community_id = db.Column(db.Integer, nullable=False, primary_key=True)
    community_name = db.Column(db.Text, nullable=False)
    community_tagline = db.Column(db.Text, nullable=True)
    community_content = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"community: ('{self.community}')"

class Post(db.Model):
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    posting_user = db.Column(db.Text, db.ForeignKey('user_access.username'), nullable=False)
    posted_date = db.Column(db.DateTime, nullable=False)
    community = db.Column(db.Text, nullable=False)
    UUID = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)

    def __repr__(self):
        return f"""\nPost {self.UUID}:
        \t-author: {self.posting_user}
        \t-posted_date: {self.posted_date}
        \t-content: {self.content}
        \t-community: {self.community}
        """

class Reply(db.Model):
    original_post_id = db.Column(db.Integer, db.ForeignKey('post.UUID'), nullable=False)
    reply_content = db.Column(db.Text, nullable=False)
    reply_user = db.Column(db.Text, db.ForeignKey('user_access.username'), nullable=False)
    reply_date = db.Column(db.DateTime, nullable=False)
    reply_UUID = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)

    def __repr__(self):
        return f"""\nReply {self.reply_UUID}:
        \t-author: {self.reply_user}
        \t-reply_date: {self.reply_date}
        \t-content: {self.reply_content}
        """