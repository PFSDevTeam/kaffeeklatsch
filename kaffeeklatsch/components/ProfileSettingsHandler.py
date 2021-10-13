#File: ProfileSettingsHandler.py
#@author: Emily Godwin, David Hovey
#Description: This file contains the python logic to handle
#   user information updates given by routes, taken in by the
#   user information change forms. It allows calls the the UserHandler
#   to update the database with the user's new tagline, password, avatar,
#   and content

from kaffeeklatsch.utilities.Hasher import Hasher
from kaffeeklatsch.utilities.UserHandler import UserHandler
from kaffeeklatsch.utilities.Errors import previousUserPassword

class ProfileSettingsHandler:

    #function to call UserHandler to update the database with new tagline
    def updateTagline(self, username, newTagline):
        UserHandler.updateTagline(username, newTagline)

    #function to call UserHandler to update the database with new password    
    def updatePassword(self, username, newPassword):
        
        #hash the new password
        newHashedPassword = Hasher.hash(newPassword)
        
        #grab the current user
        foundUser = UserHandler.getUser(username)
        
        #check to see if given password to change matches the current password in the database, raise error if True
        if(foundUser.password != newHashedPassword):
            #if not used, insert into the db
            UserHandler.updateUserPassword(username, newHashedPassword)
            return True
        else:
            #TODO: flash error
            print(f'your password has alredy been used, please select a different one')
            raise previousUserPassword
    
    #function to call UserHandler to update the database with new avatar
    def updateAvatar(self, username, newAvatar):
        UserHandler.updateAvatar(username, newAvatar)
    
    #function to call UserHandler to update the database with new userContent
    def updateUserContent(self, username, newContent):
        UserHandler.updateContent(username, newContent)