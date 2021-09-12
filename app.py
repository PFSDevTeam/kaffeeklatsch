from flask import Flask, render_template, flash, redirect, url_for, request

from components.LoginHandler import LoginHandler
from components.Errors import InvalidUsernameError, InvalidPasswordError

app = Flask(__name__)

##FLASK APP HELLO WORLD

@app.route("/")
def hello():
  #ADDED FOR TESTING
  loginHandler = LoginHandler()
  try:
    #NOTE: At this point the validLogin function either raises an error or returns true, consider removing boolean return
    validLogin = loginHandler.login("steve", "scuba")
    print(f'valid login: ' + str(validLogin))
  except InvalidUsernameError as err:
    print(err)
  except InvalidPasswordError as err:
    print(err)

  #render the html template 
  return render_template('index.html')

if __name__ == "__main__":
  app.run()