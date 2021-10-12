#File: UpVoteHandler.py
#@author: Geoff Floding, David Hovey
#Description: This file contains the python logic to handle
#   the posting of the upvote button calls to the database
#   in CommentHandler

#libraries
from kaffeeklatsch.utilities.Errors import NotAbletoPostComment
from kaffeeklatsch.utilities.CommentHandler import CommentHandler

# Class to handle the posting of comments
class UpVoteHandler:

    def incrementTally(self, original_post_id):
        try:
            print("ReplyHandler is trying to call CommentHandler")
            CommentHandler.incrementTally(original_post_id)
        except Exception as ex: 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            raise NotAbletoPostComment
