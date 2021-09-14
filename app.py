from flask import Flask, render_template, flash, redirect, url_for, request

from components.LoginHandler import LoginHandler
from utilities.Errors import InvalidUsernameError, InvalidPasswordError, UserAlreadyExistsError, UserNotFoundError
from components.RegistrationHandler import RegistrationHanlder
from forms.LoginForm import LoginForm

app = Flask(__name__)

##FLASK APP HELLO WORLD

#randomly generated secret key I may use for something later
app.config['SECRET_KEY'] = '31271d66321b32a7f3e9ad4c27106e85'

@app.route("/", methods=['POST'])
def hello():
  #ADDED FOR TESTING
  loginHandler = LoginHandler()
  form = LoginForm()
  try:
    #NOTE: At this point the validLogin function either raises an error or returns true, consider removing boolean return
    validLogin = loginHandler.login("steve", "scuba")
    print(f'valid login: ' + str(validLogin))
  except InvalidUsernameError as err:
    print(err)
  except InvalidPasswordError as err:
    print(err)
  except UserNotFoundError as err:
    print(err)

  #MORE TESTING
  regHandler = RegistrationHanlder()
  try:
    regHandler.register("steve", "scuba")
    regHandler.register("scuba", "steven")
  except UserAlreadyExistsError as err:
    print(err)

  #LOGIN IMPLEMENTATION BEGINS
  if form.validate_on_submit():
        print("form input is validated")
        inputUsername = form.username
  else:
        print("form input is incorrect")


  #render the html template 
  return render_template('login.html', form=form)

if __name__ == "__main__":
  app.run()