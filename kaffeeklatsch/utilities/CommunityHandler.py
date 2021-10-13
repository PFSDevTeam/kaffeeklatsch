#File: CommunityHandler.py
#@author: Emily Godwin
#Description: This file contains the definitions for updating
#    the database based on the Community Informaiton given

#libraries
from kaffeeklatsch.utilities.Errors import CommunityNotFoundError
from kaffeeklatsch.models.models import Community
from kaffeeklatsch import db
from datetime import datetime

class CommunityHandler:

    #check if community exists, if so return true
    @classmethod
    def checkCommunityExists(cls, communityname):
        #check if the username is present
        foundCommunity = cls.__getSelectedCommunity(communityname)
        if (foundCommunity !=  None):
            return True
        else:
            return False
    
    #find the slected community
    @classmethod
    def __getSelectedCommunity(cls, inputComm):
            #try to find the username from the loaded users
        comm = Community.query.filter_by(community_name=inputComm).first()
        if (comm != None):
            return comm
        else:
            return None
    
    @classmethod
    def getCommunity(cls, communityname):
        #check if the community is present
        foundComm = cls.__getSelectedCommunity(communityname)
        if (foundComm !=  None):
            return foundComm
        else:
            raise CommunityNotFoundError

    #insert a new community into the database
    @classmethod
    def insertCommunity(cls, communityname, tagline, content, avatar):
        newCommunityProfile = Community(community_name=communityname, community_tagline=tagline, community_content=content, community_image=avatar, community_datejoined=datetime.utcnow())
        try:
            db.session.add(newCommunityProfile)
            db.session.commit()
            return True
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return False