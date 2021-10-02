#libraries
from kaffeeklatsch.utilities.Errors import NotAbletoPostComment
from kaffeeklatsch.models.models import Post
from kaffeeklatsch.utilities.CommentHandler import CommentHandler

# Class to handle the posting of comments
class PostHandler:

    def post(self, title, content, posting_user, community):

        # Used to generate UUID
        # uUID = CommentHandler.getUUID()
        #temp uUID value
        uUID = 6

        try:
            print("PostHandler is trying to call CommentHandler")
            CommentHandler.insertComment(title, content, posting_user, community, uUID)
        except:
            raise NotAbletoPostComment