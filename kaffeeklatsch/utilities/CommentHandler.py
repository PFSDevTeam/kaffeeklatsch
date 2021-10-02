# the user handler class handles the repetative functions for the Login and registration functions

#libraries
from kaffeeklatsch.models.models import Post, UserAccess
from kaffeeklatsch import db

class CommentHandler:

    #insert a new comment into the database, posted_date is commented because we are relying on the default value input into the database
    @classmethod
    # def insertComment(cls, title, content, posting_user, posted_date, community, UUID):
    #     wholePost = Post(title=title, content=content, posting_user=posting_user, posted_date=posted_date, community=community, UUID=UUID)
    def insertComment(cls, title, content, posting_user, community, UUID):
        wholePost = Post(title=title, content=content, posting_user=posting_user, community=community, UUID=UUID)

        try:
            print("Trying to write to the DB with CommentHandler")
            db.session.add(wholePost)
            db.session.commit()
            return True
        except: 
            return False
    
    #method for returning highest UUID
    # URL for potentially helpful post https://stackoverflow.com/questions/30784456/sqlalchemy-return-a-record-filtered-by-max-value-of-a-column
    # @classmethod
    # def getUUID(cls):
    #     qry = session.query(Data).filter(
    #   Data.user_id == user_id).order_by(
    #   desc(Data.counter).limit(1)