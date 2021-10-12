# Imports for Flask.
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user
from kaffeeklatsch import app,db

# Imports for login pages.
from kaffeeklatsch.components.LoginHandler import LoginHandler
from kaffeeklatsch.utilities.Errors import InvalidUsernameError, InvalidPasswordError, UserAlreadyExistsError, UserNotFoundError
from kaffeeklatsch.forms.LoginForm import LoginForm

# Adding imports for the registration page.
from kaffeeklatsch.components.RegistrationHandler import RegistrationHandler
from kaffeeklatsch.forms.RegistrationForm import RegistrationForm

# Imports for handling Posts and Replies.
from kaffeeklatsch.forms.SortPostForm import SortPostForm
from kaffeeklatsch.forms.ReplyForm import ReplyForm
from kaffeeklatsch.forms.MakePostForm import MakePostForm
from kaffeeklatsch.forms.CommunityPainForm import CommunityPainForm
from kaffeeklatsch.components.PostHandler import PostHandler
from kaffeeklatsch.components.ReplyHandler import ReplyHandler

# Profile Settings changes forms.
from kaffeeklatsch.forms.ChangeAvatarForm import ChangeAvatarForm
from kaffeeklatsch.forms.ChangePasswordForm import ChangePasswordForm
from kaffeeklatsch.forms.ChangeTaglineForm import ChangeTaglineForm
from kaffeeklatsch.forms.ChangeContentForm import ChangeContentForm

# Community profile page import.
from kaffeeklatsch.forms.CommunityPageInfo import CommunityPageInfo

from kaffeeklatsch.models.models import UserAccess, User, Post, Community

# Imports for voting mechanism.
from kaffeeklatsch.forms.UpVoteForm import UpVoteForm
from kaffeeklatsch.components.UpVoteHandler import UpVoteHandler
from kaffeeklatsch.forms.DownVoteForm import DownVoteForm
from kaffeeklatsch.components.DownVoteHandler import DownVoteHandler

#profile settings change handler import
from kaffeeklatsch.components.ProfileSettingsHandler import ProfileSettingsHandler

#community creation page handler import
from kaffeeklatsch.components.CommunityCreationHandler import CommunityCreationHandler

#community Info Form import
from kaffeeklatsch.forms.CommunityInfoForm import CommunityInfoForm

# Flask routing for main application loging page.
@app.route("/", methods=['GET','POST'])
def login():
  loginHandler = LoginHandler()
  form = LoginForm()

  #LOGIN IMPLEMENTATION BEGINS
  if form.validate_on_submit():
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

  # Render the html template for the login page.
  return render_template('login.html', form=form)


# Here we create the route for the registration page.
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

# Here we create the route for the feed page.
@app.route('/feed', methods=['GET', 'POST'])
def feed():

  # Conditional statement verifying that user is authenticated.
  if (current_user.is_authenticated == False):
    return redirect(url_for('login')) 

  # Form and handler instantiation.
  sortPostForm = SortPostForm()
  replyForm = ReplyForm()
  makePostForm = MakePostForm()
  communityPainForm = CommunityPainForm()
  posts = Post.query.all()
  communities = Community.query.all()
  postHandler = PostHandler()
  replyHandler = ReplyHandler()
  upVoteForm = UpVoteForm()
  upVoteHandler = UpVoteHandler()
  downVoteForm = DownVoteForm()
  downVoteHandler = DownVoteHandler()

  # Grab current user and set info from DB.
  userName = current_user.username
  userInfo = User.query.filter_by(username=userName).first()

  # Conditional to check if a post needs to be submitted.
  if makePostForm.validate_on_submit():
    print("form input is validated")
    inputTitle = request.form['postTitle']
    inputContent = request.form['postContent']
    inputUsername = current_user.username
    inputCommunity = "Test Community"
    postHandler.post(inputTitle, inputContent, inputUsername, inputCommunity)
    # Reload the page & clear fields.
    return redirect(url_for('feed'))
  else:
    print("Post logic not entered.")

  # Conditional to check if a post needs to be submitted.
  if replyForm.validate_on_submit():
    print("Reply form input is validated")
    inputContent = request.form['replyContent']
    inputUsername = current_user.username
    # Get the original post ID.
    retrievedPostId = int(request.form['index'])
    originalPostFilter = filter(lambda post: post.UUID == retrievedPostId, posts)
    originalPostList = list(originalPostFilter)
    originalPost = originalPostList.pop()
    print(f'original post id: ', retrievedPostId)
    print(f'original post: ', originalPost)
    inputOriginalPostID = retrievedPostId
    # Write the post object.
    replyHandler.reply(inputOriginalPostID, inputContent, inputUsername)
    # Reload the page & clear fields.
    return redirect(url_for('feed'))
  else:
    print("Reply logic not entered.")

  # Conditional to check if a post's tally needs to be decremented.
  if request.form.get("downArrow"):
    print("Entered decrement logic.")
    # Get the original post ID.
    retrievedPostId = int(request.form['index'])
    originalPostFilter = filter(lambda post: post.UUID == retrievedPostId, posts)
    originalPostList = list(originalPostFilter)
    originalPost = originalPostList.pop()
    print(f'original post id: ', retrievedPostId)
    print(f'original post: ', originalPost)
    inputOriginalPostID = retrievedPostId
    downVoteHandler.decrementTally(inputOriginalPostID)
    # Reload the page & clear fields.
    return redirect(url_for('feed'))

  # Conditional to check if a post's tally needs to be incremented.
  if request.form.get("upArrow"):
    print("Entered increment logic.")
    # Get the original post ID.
    retrievedPostId = int(request.form['index'])
    originalPostFilter = filter(lambda post: post.UUID == retrievedPostId, posts)
    originalPostList = list(originalPostFilter)
    originalPost = originalPostList.pop()
    print(f'original post id: ', retrievedPostId)
    print(f'original post: ', originalPost)
    inputOriginalPostID = retrievedPostId
    upVoteHandler.incrementTally(inputOriginalPostID)
    # Reload the page & clear fields.
    return redirect(url_for('feed'))

  # Render the page and pass the relevant forms.
  return render_template('feed.html', 
  makePostForm=makePostForm, 
  sortPostForm=sortPostForm, 
  replyForm=replyForm, 
  communityPainForm=communityPainForm, 
  posts=posts, 
  communities=communities, 
  userInfo=userInfo,
  upVoteForm=upVoteForm, 
  downVoteForm=downVoteForm)

# Here we create the route for the profile page.
@app.route('/profilepage', methods=['GET', 'POST'])
def profilePage():
    # Redirect to feed page on logo click.
    if request.method == 'POST':
        return redirect(url_for('feed'))
    sortPostForm = SortPostForm()
    replyForm = ReplyForm()
    makePostForm = MakePostForm()
    upVoteForm = UpVoteForm()
    upVoteHandler = UpVoteHandler()
    downVoteForm = DownVoteForm()
    downVoteHandler = DownVoteHandler()
    userName = current_user.username
    userInfo = User.query.filter_by(username=userName).first()
    posts = Post.query.all()
    print(posts)

    # Render the page and pass the relevant forms.
    return render_template('profile_page.html', 
    makePostForm=makePostForm, 
    sortPostForm=sortPostForm, 
    replyForm=replyForm, 
    posts=posts, 
    userInfo=userInfo, 
    upVoteForm=upVoteForm, 
    downVoteForm=downVoteForm)

# Here we create the route for the profileSettings page.
@app.route('/profileSettingsPage',  methods=['GET', 'POST'])
def profileSettingsPage():
    profileSettingsHandler=ProfileSettingsHandler()
    changeAvatarForm = ChangeAvatarForm()
    changePasswordForm = ChangePasswordForm()
    changeTaglineForm = ChangeTaglineForm()
    changeContentForm = ChangeContentForm()
    userName=current_user.username

    # Query to pull the User db info based on given username.
    userInfo = User.query.filter_by(username=userName).first()

    # Query to pull the UserAccess db info based on given username.
    userAccessInfo = UserAccess.query.filter_by(username=userName).first()

    # Validate the submission of a change to an avatar, then re-render the page.
    if changeAvatarForm.validate_on_submit():
      print(f'change avatar valid')
      avatarChange = request.form['newAvatar']
      profileSettingsHandler.updateAvatar(userName, avatarChange)
      return redirect(url_for('profileSettingsPage'))
    else:
      print(f'change avatar invalid')

    # Validate the submission of a change to a password, then re-render the page.
    if changePasswordForm.validate_on_submit():
      print(f'change password form valid')
      newPassword = request.form['newPassword']
      profileSettingsHandler.updatePassword(userName, newPassword)
      return redirect(url_for('profileSettingsPage'))
    else:
      print(f'change password form invalid')

    # Validate the submission of a change to a tagline, then re-render the page.
    if changeTaglineForm.validate_on_submit():
      print(f'change tagline form valid')
      taglineChange = request.form['taglineChange']
      profileSettingsHandler.updateTagline(userName, taglineChange)
      return redirect(url_for('profileSettingsPage'))
    else:
      print(f'change tagline form invalid')

    # Validate the submission of a change to a ContentForm, then re-render the page.
    if changeContentForm.validate_on_submit():
      print(f'change user content form valid')
      newContent = request.form['newContent']
      profileSettingsHandler.updateUserContent(userName, newContent)
      return redirect(url_for('profileSettingsPage'))
    else:
      print(f'change content form invalid')

    # Render the page and pass the relevant forms.
    return render_template('profile_settings.html', 
    userInfo=userInfo, 
    userAccessInfo=userAccessInfo, 
    changeAvatarForm=changeAvatarForm,
    changePasswordForm=changePasswordForm,
    changeTaglineForm=changeTaglineForm,
    changeContentForm=changeContentForm)

@app.route('/communityPage', methods=['GET', 'POST'])
def communityPage():
  if request.method == 'POST':
    return redirect(url_for('feed'))
  sortPostForm = SortPostForm()
  replyForm = ReplyForm()
  makePostForm = MakePostForm()
  upVoteForm = UpVoteForm()
  upVoteHandler = UpVoteHandler()
  downVoteForm = DownVoteForm()
  downVoteHandler = DownVoteHandler()
  communityInfo = Community.query.filter_by(community_id=7).first()
  posts = Post.query.all()
  print(posts)
  userName = current_user.username
  #query to pull the User db info based on given username
  userInfo = User.query.filter_by(username=userName).first()

  # Render the page and pass the relevant forms.
  return render_template('community_page.html', 
  makePostForm=makePostForm, 
  sortPostForm=sortPostForm, 
  replyForm=replyForm, 
  posts=posts, 
  communityInfo=communityInfo, 
  upVoteForm=upVoteForm, 
  downVoteForm=downVoteForm,
  userInfo=userInfo)


# Here we create the route for logging the user out.
@app.route('/logout', methods=['GET'])
def logout():
  logout_user()
  return redirect(url_for('login'))

@app.route('/communityCreation', methods=['GET','POST'])
def communityCreation():
  communityCreationHandler = CommunityCreationHandler()
  communityInfoForm = CommunityInfoForm()
  userName=current_user.username

  #query to pull the User db info based on given username
  userInfo = User.query.filter_by(username=userName).first()

  if communityInfoForm.validate_on_submit():
    print("community form input is validated")
    communityName = request.form['communityname']
    communityTagline = request.form['communitytagline']
    communityContent = request.form['communitycontent']
    communityAvatar = request.form['communityavatar']
    communityCreationHandler.createCommunity(communityName, communityTagline, communityContent, communityAvatar)
    #redirect to communityPage?? CommunitySuccessPage (create this?)
    return redirect(url_for('feed'))
  else:
    print("community form input is incorrect")
  
  return render_template('community_creation.html', userInfo=userInfo, communityInfoForm=communityInfoForm)
