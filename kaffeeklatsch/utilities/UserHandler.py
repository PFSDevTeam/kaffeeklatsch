# the user handler class handles the repetative functions for the Login and registration functions

#libraries
from kaffeeklatsch.utilities.Errors import UserNotFoundError
from kaffeeklatsch.models.models import UserAccess, User
from kaffeeklatsch import db
from datetime import datetime

class UserHandler:

    #check if user exists, if so return true
    @classmethod
    def checkUserExists(cls, username):
        #check if the username is present
        foundUser = cls.__getSelectedUser(username)
        if (foundUser !=  None):
            return True
        else:
            return False
    
    #find the slected user
    @classmethod
    def __getSelectedUser(cls, inputUsername):
            #try to find the username from the loaded users
        user = UserAccess.query.filter_by(username=inputUsername).first()
        if (user != None):
            return user
        else:
            return None
    
    @classmethod
    def getUser(cls, username):
        #check if the username is present
        foundUser = cls.__getSelectedUser(username)
        if (foundUser !=  None):
            return foundUser
        else:
            raise UserNotFoundError

    #insert a new user into the database
    @classmethod
    def insertUser(cls, username, password):
        newUserAccess = UserAccess(username=username, password=password)
        newUserProfile = User(username=username, date_joined=datetime.utcnow())
        try:
            db.session.add(newUserAccess)
            db.session.add(newUserProfile)
            db.session.commit()
            return True
        except: 
            return False

    #update password based on user in db - Emily
    @classmethod
    def updateUserPassword(cls, username, password):
        user_info = UserAccess(username=username, password=password)
        try:
            db.session.query(user_info).update({user_info.password, password})
            db.session.commit()
            return True
        except:
            return False
    
    #update tagline in db- Emily
    @classmethod
    def updateTagline(cls, username, tagline):
        user_info = User(username=username)
        try:
            db.session.query(user_info).update({user_info.tagline, tagline})
            db.session.commit()
            return True
        except:
            return False

