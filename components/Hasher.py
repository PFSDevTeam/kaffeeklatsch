#Hasher takes in password and spits out string

import hashlib
import binascii

class Hasher:

    @staticmethod
    def hash(stringInput):
                #instantiate hasher
        hasher = hashlib.sha256()
        #salt the password with the class number
        hasher.update(b"495")
        #create byte array of input password
        byteArray = bytes(stringInput, 'utf-8')
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
