#File: CommentHandler.py
#@author: Emily Godwin
#Description: This file contains the class methods
#   to update the database based on the fields of the
#   post object

#libraries
from kaffeeklatsch.models.models import Post
from kaffeeklatsch.models.models import Reply
from kaffeeklatsch import db
from datetime import datetime

class CommentHandler:

    #insert a new comment into the database, posted_date is commented because we are relying on the default value input into the database
    @classmethod
    def insertComment(cls, title, content, posting_user, community):
        wholePost = Post(title=title, content=content, posting_user=posting_user, community=community, posted_date=datetime.utcnow(), tally=0)

        try:
            print("Trying to write to the DB with CommentHandler")
            print(wholePost)
            db.session.add(wholePost)
            db.session.commit()
            return True
        except Exception as ex: 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return False
    
    # Method for inserting a reply into the database.
    @classmethod
    def insertReply(cls, original_post_id, reply_content, reply_user):
        wholePost = Reply(original_post_id=original_post_id, reply_content=reply_content,reply_user=reply_user, reply_date=datetime.utcnow())

        try:
            print("Trying to write to the DB with CommentHandler")
            print(wholePost)
            db.session.add(wholePost)
            db.session.commit()
            return True
        except Exception as ex: 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return False
    
    # Method for incrementing the tally of votes for a post.
    @classmethod
    def incrementTally(cls, original_post_id):

        try:
            postObject = Post.query.filter_by(UUID=original_post_id).first()
            tempTally = postObject.tally
            tempTally = tempTally + 1
            postObject.tally = tempTally
            db.session.commit()
            return True
        except Exception as ex: 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return False
    
    # Method for decrementing the tally of votes for a post.
    @classmethod
    def decrementTally(cls, original_post_id):

        try:
            postObject = Post.query.filter_by(UUID=original_post_id).first()
            tempTally = postObject.tally
            tempTally = tempTally - 1
            postObject.tally = tempTally
            db.session.commit()
            return True
        except Exception as ex: 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return False
