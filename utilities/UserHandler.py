# the user handler class handles the repetative functions for the Login and registration functions

#libraries
import csv
from utilities.Errors import UserNotFoundError

#custom classes
from utilities.TempUser import User

class UserHandler:

    users = []
    FILE_NAME="credentials.csv"

        ##check user block

    #check if user exists, if so return true
    @classmethod
    def checkUserExists(cls, username):
        cls.__readFile(cls.FILE_NAME)
        for user in cls.users:
            print(f'user {user.userIndex} username: {user.loadedUsername}')
        #check if the username is present
        foundUser = cls.__getSelectedUser(username)
        #empty the users array
        cls.users = []
        if (foundUser !=  None):
            return True
        else:
            return False


    @classmethod
    def __readFile(cls, fileName):
        with open(fileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                #ensure username is lower case | strip whitespace out of password
                loadedUser = User(loadedUsername = row[0].lower(), loadedPassword = row[1].strip(), userIndex = line_count)
                cls.users.append(loadedUser)
                line_count += 1
    
    #find the slected user
    @classmethod
    def __getSelectedUser(cls, inputUsername):
        #try to find the username from the loaded users
        for user in cls.users:
            if (user.loadedUsername == inputUsername): 
                return user
        return None

        #get user block

    @classmethod
    def getUser(cls, username):
        cls.__readFile(cls.FILE_NAME)
        #check if the username is present
        foundUser = cls.__getSelectedUser(username)
        #empty the users array
        cls.users = []
        if (foundUser !=  None):
            return foundUser
        else:
            raise UserNotFoundError
