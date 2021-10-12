#File: PostHandler.py
#@author: Geoff Floding, David Hovey, Ryan Dombek
#Description: This file contains the python logic to handle
#   calls to CommentHandler which pushes to the database

#libraries
from kaffeeklatsch.utilities.Errors import NotAbletoPostComment
from kaffeeklatsch.utilities.CommentHandler import CommentHandler

# Class to handle the posting of comments
class PostHandler:

    def post(self, title, content, posting_user, community):
        try:
            print("PostHandler is trying to call CommentHandler")
            CommentHandler.insertComment(title, content, posting_user, community)
        except Exception as ex: 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            raise NotAbletoPostComment
