#logger class
from datetime import datetime

class Logger:
    def __init__(self):
        super().__init__()
    #write the invalid attempt string
    def log_invalid_attempt(self, invalid_attempt_string):
        with open('logfile.csv', 'a') as logfile:
            currentDate = datetime.now()
            logfile.write(f"{invalid_attempt_string},{currentDate}\n")