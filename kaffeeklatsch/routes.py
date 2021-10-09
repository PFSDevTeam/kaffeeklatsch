
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
from kaffeeklatsch.components.PostHandler import PostHandler # For the posting of comments
from kaffeeklatsch.components.ReplyHandler import ReplyHandler

#profile page imports
from kaffeeklatsch.forms.ProfilePageInfo import ProfilePageInfo

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

@app.route('/feed', methods=['GET', 'POST'])
def feed():

    if (current_user.is_authenticated == False):
      return redirect(url_for('login')) 

    #main logic path
    sortPostForm = SortPostForm()
    replyForm = ReplyForm()
    makePostForm = MakePostForm()
    communityPainForm = CommunityPainForm()
    posts = Post.query.all()
    postHandler = PostHandler()
    replyHandler = ReplyHandler()
    # print(posts)
    # load posts here

    if makePostForm.validate_on_submit():
      print("form input is validated")
      inputTitle = request.form['postTitle']
      inputContent = request.form['postContent']
      inputUsername = current_user.username
      # not passing time, using default value in model
      inputCommunity = "Test Community" # Will need to be updated with ability to pull relevant community
      postHandler.post(inputTitle, inputContent, inputUsername, inputCommunity)
      #reload the page & clear fields
      return redirect(url_for('feed'))
    else:
      print("you're stuff still isnt workin (post)")

    if replyForm.validate_on_submit():
      print("Reply form input is validated")
      inputContent = request.form['replyContent']
      inputUsername = current_user.username
      # not passing time, using default value in model
      inputCommunity = "Test Community" # Will need to be updated with ability to pull relevant community
      inputOriginalPostID = 1
      replyHandler.reply(inputOriginalPostID, inputContent, inputUsername, inputCommunity)
      #reload the page & clear fields
      return redirect(url_for('feed'))
    else:
      print("reply you're stuff still isnt workin (reply)")

    return render_template('feed.html', makePostForm=makePostForm, sortPostForm=sortPostForm, replyForm=replyForm, communityPainForm=communityPainForm, posts=posts)

#profile page routing
@app.route('/profilepage')
def profilePage():
  #main logic path
  sortPostForm = SortPostForm()
  replyForm = ReplyForm()
  makePostForm = MakePostForm()
  posts = Post.query.all()
  print(posts)
  #TODO: logic to implement Profile Page info to be grabbed from the current user in the database
  return render_template('profile_page.html', makePostForm=makePostForm, sortPostForm=sortPostForm, replyForm=replyForm, posts=posts, ProfilePageInfo=ProfilePageInfo)

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('login'))