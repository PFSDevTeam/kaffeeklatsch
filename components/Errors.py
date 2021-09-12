class Error(Exception):
    #custom error base class
    pass

class InvalidUsernameError(Error):
    #invalid username
    DEFAULT_MESSAGE = "Error: invalid username"

    def __init__(self):
        super().__init__(self.DEFAULT_MESSAGE)

class InvalidPasswordError(Error):
    #invalid password
    DEFAULT_MESSAGE = "Error: invalid password"

    def __init__(self):
        super().__init__(self.DEFAULT_MESSAGE)