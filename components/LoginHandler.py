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
        self.userName = inputUser
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
        #return result

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

    def read_file(self, fileName):
        with open(fileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                loadedUser = self.User(loadedUsername = row[0], loadedPassword = row[1], userIndex = line_count)
                self.users.append(loadedUser)
                line_count += 1

    
    class User:
        def __init__(self, loadedUsername, loadedPassword, userIndex):
            self.loadedUsername = loadedUsername
            self.loadedPassword = loadedPassword
            self.userIndex = userIndex
    # def comparePasswords(retrievedPass, inputPass):
