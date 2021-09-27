from flask import render_template, flash, redirect, url_for, request, session
from flask_login import login_user
from kaffeeklatsch import app,db

#login imports
from kaffeeklatsch.components.LoginHandler import LoginHandler
from kaffeeklatsch.utilities.Errors import InvalidUsernameError, InvalidPasswordError, UserAlreadyExistsError, UserNotFoundError
from kaffeeklatsch.forms.LoginForm import LoginForm

# Adding imports for the registration page
from kaffeeklatsch.components.RegistrationHandler import RegistrationHandler
from kaffeeklatsch.forms.RegistrationForm import RegistrationForm

#post imports
from kaffeeklatsch.forms.SortPostForm import SortPostForm
from kaffeeklatsch.forms.ReplyForm import ReplyForm
from kaffeeklatsch.forms.MakePostForm import MakePostForm
from kaffeeklatsch.forms.CommunityPainForm import CommunityPainForm

#TEST
from kaffeeklatsch.models.models import UserAccess, User, Post, Community


@app.route("/", methods=['GET','POST'])
def login():
  #LOGIN TESTING
  loginHandler = LoginHandler()
  form = LoginForm()

#   try:
#     #NOTE: At this point the validLogin function either raises an error or returns true, consider removing boolean return
#     validLogin = loginHandler.login("steve", "scuba")
#     # validLogin = loginHandler.login("scuba", "steven")
#     # validLogin = loginHandler.login("jeff", "guy")
#     print(f'valid login: ' + str(validLogin))
#   except InvalidUsernameError as err:
#     print(err)
#   except InvalidPasswordError as err:
#     print(err)
#   except UserNotFoundError as err:
#     print(err)

  #LOGIN IMPLEMENTATION BEGINS
  if form.validate_on_submit():
    #flash messaging doesn't currently work 
    # flash(f'login successfull!', 'success')
    # session["username"] = request.form['username']
    if (loginHandler.login(form.username.data, form.password.data)):
      user = User.query.filter_by(username=form.username.data).first()
      login_user(user)
    print(f'retrived user: {user}')
    return redirect(url_for('feed'))
  else:
    print(form.errors)
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

      #REGISTRATION TESTING
  # regHandler = RegistrationHandler()
  # try:
  #   # regHandler.register("steve", "scuba")
  #   regHandler.register("scuba", "steven")
  #   # regHandler.register("jeff", "guy")
  #   print('registered')
  # except UserAlreadyExistsError as err:
  #   print(err)
  
  return render_template('register.html', form=registrationForm)

@app.route('/feed')
def feed():

    #DB TEST
    # print(f'users modesl list: {UserAccess.query.all()}')
    # print(f'users modesl list: {User.query.all()}')
    # print(f'community model list: {Community.query.all()}')
    # print(f'post model list: \n {Post.query.all()}')
      
    #check session cookies, if it's not set redirect to login
    # if (session.get("username") == None):
    #     return redirect(url_for('login'))

    #main logic path
    sortPostForm = SortPostForm()
    replyForm = ReplyForm()
    makePostForm = MakePostForm()
    communityPainForm = CommunityPainForm()
    # load posts here
    return render_template('feed.html', makePostForm=makePostForm, sortPostForm=sortPostForm, replyForm=replyForm, communityPainForm=communityPainForm)