#handles writing new users

#libraries
import csv

#custom classes
from utilities.Hasher import Hasher
from utilities.Errors import PasswordsDoNotMatch, UserAlreadyExistsError, PasswordsDoNotMatch
from utilities.TempUser import User

class RegistrationHanlder:

    #global instance variables
    users = []
    FILE_NAME="credentials.csv"

    def register(self, inputUser, inputPass):
        #local variable assignments
        self.userName = inputUser.lower()
        self.password = inputPass

        #hash the input
        stringHashedPassword = Hasher.hash(self.password)
        #if user is not found add username & hashed password
        self.checkForExistingUser(self.userName)
        self.writeCredentials(self.userName, stringHashedPassword)

    def read_file(self, fileName):
        with open(fileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                #ensure username is lower case | strip whitespace out of password
                loadedUser = User(loadedUsername = row[0].lower(), loadedPassword = row[1].strip(), userIndex = line_count)
                self.users.append(loadedUser)
                line_count += 1

    def writeCredentials(self, username, password):
        #write the username and hashed pass to the file
        with open(self.FILE_NAME, mode='w') as userFiles:
            credential_writer = csv.writer(userFiles, delimiter=',', quotechar='"')
            credential_writer.writerow(username, password)

    def checkForExistingUser(self, username):
        #check to see if the username exists already, if so raise a user already exists exception
        self.read_file(self.FILE_NAME)
        for user in self.users:
            print(f'user {user.userIndex} username: {user.loadedUsername}')
        #check if the username is present
        foundUser = self.getSelectedUser(username)
        #empty the users array
        self.users = []

        if (foundUser != None):
            print("user already exists")
            raise self.UserAlreadyExistsError()