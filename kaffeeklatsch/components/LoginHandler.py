#File: LoginHandler.py
#@author: Ryan Dombek, Geoff Floding, Majestic Dwyer, David Hovey
#Description: This file contains the python logic to handle
#   the login form routing to the database in UserHandler
#   on init: accept username and password

#custom clases
from kaffeeklatsch.utilities.Errors import InvalidPasswordError, InvalidUsernameError, UserNotFoundError
from kaffeeklatsch.utilities.Hasher import Hasher
from kaffeeklatsch.utilities.UserHandler import UserHandler

class LoginHandler:

    users = []
    FILE_NAME="credentials.csv"

    def login(self, inputUser, inputPass):
        username = inputUser.lower()
        password = inputPass

        #print the username
        print("username: " + username)
        #hash the password
        stringHashedPassword = Hasher.hash(password)
        #print the password
        print(f'hashed password: {stringHashedPassword}')

        #if the user is not present, raise invalid username error
        if not (UserHandler.checkUserExists(username)):
            print('Login Handler: no found user')
            raise InvalidUsernameError()
        else:
            #if user does exist, retrieve them and check the password
            try:
                foundUser = UserHandler.getUser(username)
                print(f'found user: {foundUser}')
                #check to see if the passwords match
                if (self.comparePasswords(foundUser.password, stringHashedPassword)):
                    print(f'passwords match')
                    return True
                else:
                    #if the passwords do not match, raise invalid password error
                    print(f'passwords do not match')
                    raise InvalidPasswordError
                    # return False
            except UserNotFoundError as err:
                #something went wrong on the program side and the user that was found as true did not get retrieved
                    #this check is currently redundant
                raise

    def comparePasswords(self, retrievedPass, inputPass):
        print(f'input password: {inputPass}\n' +
            f'retrieved password: {retrievedPass}')
        if (retrievedPass == inputPass):
            return True
        else: 
            return False
