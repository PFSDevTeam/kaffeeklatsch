from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user
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

  #LOGIN IMPLEMENTATION BEGINS
  if form.validate_on_submit():
    #flash messaging doesn't currently work 
    # flash(f'login successfull!', 'success')
    try:
      if (loginHandler.login(form.username.data, form.password.data)):
          user = User.query.filter_by(username=form.username.data).first()
      login_user(user)
      print(f'retrived user: {user}')
      return redirect(url_for('feed'))
    except InvalidUsernameError as err:
      print(err)
    except InvalidPasswordError as err:
      print(err)
    except UserNotFoundError as err:
      print(err)
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
  
  #LOGIN IMPLEMENTATION BEGINS
  if registrationForm.validate_on_submit():
    print("form input is validated")
    inputUsername = request.form['username']
    inputPassword = request.form['password']
    registrationHandler.register(inputUsername, inputPassword)

    #REDIRECT TO LOGIN
    return redirect(url_for('login'))
  else:
    print("form input is incorrect")
  
  return render_template('register.html', form=registrationForm)

@app.route('/feed')
def feed():

    if (current_user.is_authenticated == False):
      return redirect(url_for('login')) 

    #main logic path
    sortPostForm = SortPostForm()
    replyForm = ReplyForm()
    makePostForm = MakePostForm()
    communityPainForm = CommunityPainForm()
    posts = Post.query.all();
    print(posts);
    # load posts here
    return render_template('feed.html', makePostForm=makePostForm, sortPostForm=sortPostForm, replyForm=replyForm, communityPainForm=communityPainForm, posts=posts)

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('login'))