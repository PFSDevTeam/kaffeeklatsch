# the user handler class handles the repetative functions for the Login and registration functions

#libraries
import sqlite3
from utilities.Errors import UserNotFoundError

#custom classes
from utilities.TempUser import User

class UserHandler:

    FILE_NAME="credentials.csv"

    #DB Creation
    # user_db = sqlite3.connect('db_files/users.db')
    # db_cursor = user_db.cursor()
    # db_cursor.execute("CREATE TABLE users (username TEXT NOT NULL PRIMARY KEY, password TEXT NOT NULL)")
    # db_cursor.execute("INSERT INTO users VALUES ('steve', '432c19c7ecdc9ef6884d01b21bd306ddd4b21d4ee139f10358cf5c1b7f113904')")
    # user_db.commit()
    # db_cursor.execute("SELECT * FROM users")
    # print(f'resutls: {db_cursor.fetchone()}')
    # user_db.close()

        ##check user block

    #check if user exists, if so return true
    @classmethod
    def checkUserExists(cls, username):
        #check if the username is present
        foundUser = cls.__getSelectedUser(username)
        #empty the users array
        cls.users = []
        if (foundUser !=  None):
            return True
        else:
            return False
    
    #find the slected user
    @classmethod
    def __getSelectedUser(cls, inputUsername):
            #try to find the username from the loaded users
        #db commection
        user_db = sqlite3.connect("db_files/users.db")
        db_cursor = user_db.cursor()
        with user_db:
            #run query
            db_cursor.execute("SELECT * FROM users WHERE username=:username", {'username': inputUsername})
            results = db_cursor.fetchone()
            if not (results == None):
                #user found
                requestedUser = User(loadedUsername=results[0].lower(), loadedPassword=results[1].strip(), userIndex=0)
                return requestedUser
            else:
                #user was not found
                return None
    

    @classmethod
    def getUser(cls, username):
        #check if the username is present
        foundUser = cls.__getSelectedUser(username)
        #empty the users array
        cls.users = []
        if (foundUser !=  None):
            return foundUser
        else:
            raise UserNotFoundError

    #insert a new user into the database
    @classmethod
    def insertUser(cls, username, password):
            user_db = sqlite3.connect("db_files/users.db")
            db_cursor = user_db.cursor()
            with user_db:
                try:
                    db_cursor.execute("INSERT INTO users VALUES ('%s', '%s')" % (username, password))
                    return True
                except:
                    return False