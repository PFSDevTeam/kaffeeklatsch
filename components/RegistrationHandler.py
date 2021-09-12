#handles writing new users

#libraries

#custom classes
from components.Hasher import Hasher
from components.Errors import UserAlreadyExistsError


class RegistrationHanlder:

    #global instance variables
    FILE_NAME="credentials.csv"

    def __init__(self, inputUserName, inputPassword):
        #TODO: remove pass after implementation
        pass

    def regirster(self, username, password):
        #TODO: remove pass after implementation
        pass
            #driver function for the rest of the functions
        #check if user name already exists, if so, throw error 
        #if user does not exist, hash the password
        #call  the write function and raise any file exceptions that may come up

    def writeCredentials(username, password):
        #TODO: remove pass after implementation
        pass
        #write the username and hashed pass to the file

    def checkForExistingUser(username):
        #TODO: remove pass after implementation
        pass
        #check to see if the username exists already, if so raise a user already exists exception
        