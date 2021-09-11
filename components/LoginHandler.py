# on init we're going to accept username and password
# Login Handler should be created in the form On submit section so as to scope it to pressing the login button

import hashlib
import binascii
import csv

class LoginHandler:

    users = []
    FILE_NAME="credentials.csv"

    def __init__(self, inputUser, inputPass):
        #assign the local variables
        #convert input  username to lowercase
        self.userName = inputUser.lower()
        self.password = inputPass

        #print the username
        print("username: " + self.userName)
        #hash the password
        stringHashedPassword = self.hashedPass(self.password)
        #print the password
        print(f'hashed password: {stringHashedPassword}')

            #compare the username and hashed password against stored values
        #get access list
        self.read_file(self.FILE_NAME)
        for user in self.users:
            print(f'user {user.userIndex} username: {user.loadedUsername}')
        #check if the username is present
        foundUser = self.getSelectedUser(inputUser)
        print(f'found user: {foundUser}')
        #check to see if the passwords match
        if (self.comparePasswords(foundUser.loadedPassword, stringHashedPassword)):
            print(f'passwords match')
            return None
        else:
            print(f'passwords do not match')
            return None

    def hashedPass(self, stringPassword):
            #hash the string password
        #instantiate hasher
        hasher = hashlib.sha256()
        #salt the password with the class number
        hasher.update(b"495")
        #create byte array of input password
        byteArray = bytes(stringPassword, 'utf-8')
        #hash the input password
        hasher.update(byteArray)
        #output the digest of the hashed result
        hashedPassword = hasher.digest()
        #translate the hashed password
        hashedPassResult = binascii.hexlify(hashedPassword)
        #decode it to string
        decodedPassword = hashedPassResult.decode()
        #return the decoded password
        return decodedPassword

    # retrieve the username and pasword from the credentials file
    def read_file(self, fileName):
        with open(fileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                #ensure username is lower case | strip whitespace out of password
                loadedUser = self.User(loadedUsername = row[0].lower(), loadedPassword = row[1].strip(), userIndex = line_count)
                self.users.append(loadedUser)
                line_count += 1
    
    #find the slected user
    def getSelectedUser(self, inputUsername):
        #try to find the username from the loaded users
        for user in self.users:
            if (user.loadedUsername == inputUsername): 
                return user
        return None


    def comparePasswords(self, retrievedPass, inputPass):
        print(f'input password: {inputPass}\n' +
            f'retrieved password: {retrievedPass}')
        if (retrievedPass == inputPass):
            return True
        else: 
            return False

    #user class for the purpose of holding usernames and passwords in the login handler
    class User:
        def __init__(self, loadedUsername, loadedPassword, userIndex):
            self.loadedUsername = loadedUsername
            self.loadedPassword = loadedPassword
            self.userIndex = userIndex

        def __repr__(self):
            return (f"\n\tUser indedx: {self.userIndex}" +
                    f"\n\tUsername: {self.loadedUsername}")

        def __str__(self):
            #iterate index + 1 for readability
            return (f"\n\tUser indedx: {self.userIndex}" +
                    f"\n\tUsername: {self.loadedUsername}")
