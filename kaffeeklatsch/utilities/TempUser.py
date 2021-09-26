#THIS USER CLASS SHOULD ONLY BE USED FOR TEMPORARILY HOLDING USER OBJECTS AND NOT FOR FULL USER REPRESENTATIONS

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
