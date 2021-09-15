#handles writing new users

#libraries
import csv

#custom classes
from utilities.Hasher import Hasher
from utilities.Errors import UserAlreadyExistsError
from utilities.UserHandler import UserHandler

class RegistrationHandler:

    #global instance variables
    FILE_NAME="credentials.csv"

    def register(self, inputUser, inputPass):
        #local variable assignments
        self.username = inputUser.lower()
        self.password = inputPass

        #hash the input
        stringHashedPassword = Hasher.hash(self.password)
        #if user is not found add username & hashed password
        if not (UserHandler.checkUserExists(self.username)):
            #if user does not already exist, insert into db
            UserHandler.insertUser(self.username, stringHashedPassword)
        else:
            #if user exists, raise error
            raise UserAlreadyExistsError