#File: RegistrationHandler.py
#@author: Ryan Dombek, Geoff Floding
#Description: This file contains the python logic to handle
#   calls to UserHandler to post to the database

#custom classes
from kaffeeklatsch.utilities.Hasher import Hasher
from kaffeeklatsch.utilities.Errors import UserAlreadyExistsError
from kaffeeklatsch.utilities.UserHandler import UserHandler

class RegistrationHandler:

    def register(self, inputUser, inputPass):
        #local variable assignments
        username = inputUser.lower()
        password = inputPass

        #hash the input
        stringHashedPassword = Hasher.hash(password)
        #if user is not found add username & hashed password
        if not (UserHandler.checkUserExists(username)):
            #if user does not already exist, insert into db
            print(f'Calling UserHandler.insertHandler() to insert new user into DB.')
            print(f'received user variable: {username}')
            print(f'hashed password variable {stringHashedPassword}')
            UserHandler.insertUser(username, stringHashedPassword)
        else:
            #if user exists, raise error
            raise UserAlreadyExistsError
