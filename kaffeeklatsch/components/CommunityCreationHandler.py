#File: ProfileSettingsHandler.py
#@author: Emily Godwin, David Hovey
#Description: This file contains the python logic to handle
#   user information updates given by routes, taken in by the
#   user information change forms. It allows calls the the UserHandler
#   to update the database with the user's new tagline, password, avatar,
#   and content

from kaffeeklatsch.utilities.CommunityHandler import CommunityHandler
from kaffeeklatsch.utilities.Errors import CommunityAlreadyExistsError

class CommunityCreationHandler:
    def createCommunity(self, communityname, tagline, content, avatar):        
        if not (CommunityHandler.checkCommunityExists(communityname)):
            CommunityHandler.insertCommunity(communityname, tagline, content, avatar)
        else:
            raise CommunityAlreadyExistsError