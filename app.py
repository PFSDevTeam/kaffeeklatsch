from flask import Flask, render_template, flash, redirect, url_for, request

from components.LoginHandler import LoginHandler
from utilities.Errors import InvalidUsernameError, InvalidPasswordError, UserAlreadyExistsError, UserNotFoundError
from forms.LoginForm import LoginForm

# Adding imports for the registration page
from components.RegistrationHandler import RegistrationHandler
from forms.RegistrationForm import RegistrationForm

#post imports
from forms.SortPostForm import SortPostForm
from forms.ReplyForm import ReplyForm
from forms.MakePostForm import MakePostForm

app = Flask(__name__)

##FLASK APP HELLO WORLD

#randomly generated secret key I may use for something later
app.config['SECRET_KEY'] = '31271d66321b32a7f3e9ad4c27106e85'

@app.route("/", methods=['GET','POST'])
def hello():
  #LOGIN TESTING
  loginHandler = LoginHandler()
  form = LoginForm()
  try:
    #NOTE: At this point the validLogin function either raises an error or returns true, consider removing boolean return
    validLogin = loginHandler.login("steve", "scuba")
    # validLogin = loginHandler.login("scuba", "steven")
    # validLogin = loginHandler.login("jeff", "guy")
    print(f'valid login: ' + str(validLogin))
  except InvalidUsernameError as err:
    print(err)
  except InvalidPasswordError as err:
    print(err)
  except UserNotFoundError as err:
    print(err)

  #REGISTRATION TESTING
  # regHandler = RegistrationHandler()
  # try:
  #   # regHandler.register("steve", "scuba")
  #   regHandler.register("scuba", "steven")
  #   # regHandler.register("jeff", "guy")
  #   print('registered')
  # except UserAlreadyExistsError as err:
  #   print(err)

  #LOGIN IMPLEMENTATION BEGINS
  if form.validate_on_submit():
        print("form input is validated")
        # attempt to validate the login
          #if login is valid 
            #set session cookie
            #redirect to feed page
          #if login is not valid 
            #report errors
  else:
        print("form input is incorrect")


  #render the html template 
  return render_template('login.html', form=form)


# Here we create the route for the registration page
@app.route('/register', methods=['GET','POST'])
def register():
  registrationHandler = RegistrationHandler()
  registrationForm = RegistrationForm()
  #testing 
  loginHandler = LoginHandler()
  
  #LOGIN IMPLEMENTATION BEGINS
  if registrationForm.validate_on_submit():
    print("form input is validated")
    inputUsername = request.form['username']
    inputPassword = request.form['password']
    registrationHandler.register(inputUsername, inputPassword)
    validLogin = loginHandler.login(inputUsername, inputPassword)
    print(f'was our login successful?: {validLogin}')

    #REDIRECT TO LOGIN
    return redirect(url_for('hello'))
  else:
    print("form input is incorrect")
  
  return render_template('register.html', form=registrationForm)

@app.route('/feed')
def feed():
  #implement wrapping if statement to check session cookie
    #if session cookie is valid
      #continue to render user content
    #if session cookie is not valid
      #redirect to login page
  sortPostForm = SortPostForm()
  replyForm = ReplyForm()
  makePostForm = MakePostForm()
  # load posts here
  return render_template('feed.html', makePostForm=makePostForm, sortPostForm=sortPostForm, replyForm=replyForm)

if __name__ == "__main__":
  app.run()