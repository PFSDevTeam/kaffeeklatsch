#File: ProfileSettingsHandler.py
#@author: Emily Godwin
#Description: This file contains the python logic to handle
#   user information updates in profile settings

from kaffeeklatsch.utilities.Hasher import Hasher
from kaffeeklatsch.utilities.UserHandler import UserHandler
from kaffeeklatsch.utilities.Errors import previousUserPassword

class ProfileSettingsHandler:

    def updateInfo(self, userInfo, userAccessInfo, taglineChange, newPassword):
        #update the tagline - User db
        UserHandler.updateTagline(userInfo.username, taglineChange)
        #local variable assignments
        password = userInfo.password
        newPass = newPassword
        #hash the input
        newHashedPassword = Hasher.hash(newPass)
        foundUser = UserHandler.getUser(userInfo.username)
        #check to see if given password to change matches the current password in the database, raise error if True
        if(foundUser.password != newHashedPassword):
            #if not used, insert into the db
            UserHandler.updateUserPassword(userInfo.username, password)
            return True
        else:
            print(f'your password has alredy been used, please select a different one')
            raise previousUserPassword

    #function to compare the passwords given by the UserAccess userInfo and the newHashedPassword
    def comparePasswords(self, retrievedPass, inputPass):
        print(f'input password: {inputPass}\n' +
            f'retrieved password: {retrievedPass}')
        if (retrievedPass == inputPass):
            return True
        else: 
            return False
