#libraries
from kaffeeklatsch.utilities.Errors import NotAbletoPostComment
from kaffeeklatsch.utilities.CommentHandler import CommentHandler

# Class to handle the posting of comments
class DownVoteHandler:

    def decrementTally(self, original_post_id):

        try:
            print("ReplyHandler is trying to call CommentHandler")
            CommentHandler.decrementTally(original_post_id)
        except Exception as ex: 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            raise NotAbletoPostComment