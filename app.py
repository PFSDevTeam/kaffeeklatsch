from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

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
from forms.CommunityPainForm import CommunityPainForm

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_files/application_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Session(app)

#randomly generated secret key I may use for something later
app.config['SECRET_KEY'] = '31271d66321b32a7f3e9ad4c27106e85'

@app.route("/", methods=['GET','POST'])
def login():
  #LOGIN TESTING
  loginHandler = LoginHandler()
  form = LoginForm()

  #SESSION TESTING

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
        session["username"] = request.form['username']
        return redirect(url_for('feed'))
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
    return redirect(url_for('login'))
  else:
    print("form input is incorrect")
  
  return render_template('register.html', form=registrationForm)

@app.route('/feed')
def feed():
      
  #check session cookies, if it's not set redirect to login
  if (session.get("username") == None):
    return redirect(url_for('login'))

  #main logic path
  sortPostForm = SortPostForm()
  replyForm = ReplyForm()
  makePostForm = MakePostForm()
  communityPainForm = CommunityPainForm()
  # load posts here
  return render_template('feed.html', makePostForm=makePostForm, sortPostForm=sortPostForm, replyForm=replyForm, communityPainForm=communityPainForm)

if __name__ == "__main__":
  app.run()