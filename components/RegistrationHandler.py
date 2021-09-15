#handles writing new users

#libraries
import csv

#custom classes
from utilities.Hasher import Hasher
from utilities.Errors import UserAlreadyExistsError
from utilities.UserHandler import UserHandler

class RegistrationHanlder:

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
            #if user does not already exist, do studd
            self.writeCredentials(self.username, stringHashedPassword)
        else:
            #if user exists, raise error
            raise UserAlreadyExistsError

"""     def writeCredentials(self, username, password):
        #write the username and hashed pass to the file
        with open(self.FILE_NAME, mode='a', newline='') as userFiles:
            credential_writer = csv.writer(userFiles)
            credential_writer.writerow([username, password])
            userFiles.close() """
    
    # version of writeCedentials to use the DB
    def writeCredentials(self, username, password):
        
