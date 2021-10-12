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

class UserAlreadyExistsError(Error):
    #user already exists
    DEFAULT_MESSAGE = "Error: user already exists"

    def __init__(self):
        super().__init__(self.DEFAULT_MESSAGE)

class UserNotFoundError(Error):
    #user not found
    DEFAULT_MESSAGE = "Error: user not found"

    def __init__(self):
        super().__init__(self.DEFAULT_MESSAGE)

class PasswordsDoNotMatch(Error):
    #passwords do not math
    DEFAULT_MESSAGE = "Error: The passwords you entered do not match"

    def __init__(self):
        super().__init__(self.DEFAULT_MESSAGE)

class NotAbletoPostComment(Error):
    # Not able to post a comment
    DEFAULT_MESSAGE = "Error: Not able to post comment"

    def __init__(self):
        super().__init__(self.DEFAULT_MESSAGE)

#error to throw if previous password used - @author:Emily
class previousUserPassword(Error):
    #password matches current during attempt to change
    DEFAULT_MESSAGE = "Error: This password could not be set, it has already been used"
    
    def __init__(self):
        super().__init__(self.DEFAULT_MESSAGE)

#error to throw if community not found - @author:Emily
class CommunityNotFoundError(Error):
    #community not found
    DEFAULT_MESSAGE = "Error: community not found"

    def __init__(self):
        super().__init__(self.DEFAULT_MESSAGE)  

class CommunityAlreadyExistsError(Error):
    #user already exists
    DEFAULT_MESSAGE = "Error: community already exists"

    def __init__(self):
        super().__init__(self.DEFAULT_MESSAGE)