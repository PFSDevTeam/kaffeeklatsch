from datetime import datetime
from kaffeeklatsch import db

class UserAccess(db.Model):
    username = db.Column(db.Text, nullable=False, unique=True, primary_key=True)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.password}')"