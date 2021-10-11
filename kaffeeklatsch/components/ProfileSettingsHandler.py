#File: ProfileSettingsHandler.py
#@author: Emily Godwin
#Description: This file contains the python logic to handle
#   user information updates in profile settings

from kaffeeklatsch.utilities.Hasher import Hasher
from kaffeeklatsch.utilities.UserHandler import UserHandler
from kaffeeklatsch.utilities.Errors import previousUserPassword

class ProfileSettingsHandler:

    def updateTagline(self, username, newTagline):
        UserHandler.updateTagline(username, newTagline)
    
    def updatePassword(self, username, newPassword):
        newHashedPassword = Hasher.hash(newPassword)
        foundUser = UserHandler.getUser(username)
        #check to see if given password to change matches the current password in the database, raise error if True
        if(foundUser.password != newHashedPassword):
            #if not used, insert into the db
            UserHandler.updateUserPassword(username, newHashedPassword)
            return True
        else:
            print(f'your password has alredy been used, please select a different one')
            raise previousUserPassword
    
    def updateAvatar(self, username, newAvatar):
        newAvatar = newAvatar + "_avatar.png"
        UserHandler.updateAvatar(username, newAvatar)