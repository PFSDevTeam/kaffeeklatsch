#File: ReplyHandler.py
#@author: DavidHovey
#Description: This file contains the python logic to handle
#   the Reply posting on a Post. Sends to CommentHandler to
#   update the database

#libraries
from kaffeeklatsch.utilities.Errors import NotAbletoPostComment
from kaffeeklatsch.utilities.CommentHandler import CommentHandler

# Class to handle the posting of comments
class ReplyHandler:

    def reply(self, original_post_id, reply_content, reply_user):
        try:
            print("ReplyHandler is trying to call CommentHandler")
            CommentHandler.insertReply(original_post_id, reply_content, reply_user)
        except Exception as ex: 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            raise NotAbletoPostComment
