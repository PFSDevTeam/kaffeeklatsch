
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

#Profile Settings changes forms
from kaffeeklatsch.forms.ChangeAvatarForm import ChangeAvatarForm
from kaffeeklatsch.forms.ChangePasswordForm import ChangePasswordForm
from kaffeeklatsch.forms.ChangeTaglineForm import ChangeTaglineForm
from kaffeeklatsch.forms.ChangeContentForm import ChangeContentForm

#community profile page import
from kaffeeklatsch.forms.CommunityPageInfo import CommunityPageInfo

#profile settings change handler
from kaffeeklatsch.components.ProfileSettingsHandler import ProfileSettingsHandler


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
    communityInfo = Community.query.filter_by(community_id=2).first()
    posts = Post.query.all()
    postHandler = PostHandler()
    replyHandler = ReplyHandler()

    #grab current user and set info from db
    userName = current_user.username
    userInfo = User.query.filter_by(username=userName).first()
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
      #get the original post ID
      retrievedPostId = int(request.form['index'])
      originalPostFilter = filter(lambda post: post.UUID == retrievedPostId, posts)
      originalPostList = list(originalPostFilter)
      originalPost = originalPostList.pop()
      print(f'original post id: ', retrievedPostId)
      print(f'original post: ', originalPost)
      inputOriginalPostID = retrievedPostId
      #write the post object
      replyHandler.reply(inputOriginalPostID, inputContent, inputUsername)
      #reload the page & clear fields
      return redirect(url_for('feed'))
    else:
      print("reply you're stuff still isnt workin (reply)")

    return render_template('feed.html', makePostForm=makePostForm, sortPostForm=sortPostForm, replyForm=replyForm, communityPainForm=communityPainForm, communityInfo=communityInfo, posts=posts, userInfo=userInfo)

#profile page routing
@app.route('/profilepage', methods=['GET', 'POST'])
def profilePage():
    #redirect to feed page on logo click
    if request.method == 'POST':
        return redirect(url_for('feed'))
    sortPostForm = SortPostForm()
    replyForm = ReplyForm()
    makePostForm = MakePostForm()
    userName = current_user.username
    userInfo = User.query.filter_by(username=userName).first()
    posts = Post.query.all()
    print(posts)
    return render_template('profile_page.html', makePostForm=makePostForm, sortPostForm=sortPostForm, replyForm=replyForm, posts=posts, userInfo=userInfo)

#profile settings page routing
@app.route('/profileSettingsPage',  methods=['GET', 'POST'])
def profileSettingsPage():
    profileSettingsHandler=ProfileSettingsHandler()
    changeAvatarForm = ChangeAvatarForm()
    changePasswordForm = ChangePasswordForm()
    changeTaglineForm = ChangeTaglineForm()
    changeContentForm = ChangeContentForm()
    userName=current_user.username

    #query to pull the User db info based on given username
    userInfo = User.query.filter_by(username=userName).first()

    #query to pull the UserAccess db info based on given username
    userAccessInfo = UserAccess.query.filter_by(username=userName).first()

      #forms

    #change avatar
    if changeAvatarForm.validate_on_submit():
      print(f'change avatar valid')
      avatarChange = request.form['newAvatar']
      profileSettingsHandler.updateAvatar(userName, avatarChange)
      return redirect(url_for('profileSettingsPage'))
    else:
      print(f'change avatar invalid')

    if changePasswordForm.validate_on_submit():
      print(f'change password form valid')
      newPassword = request.form['newPassword']
      profileSettingsHandler.updatePassword(userName, newPassword)
      return redirect(url_for('profileSettingsPage'))
    else:
      print(f'change password form invalid')

    if changeTaglineForm.validate_on_submit():
      print(f'change tagline form valid')
      taglineChange = request.form['taglineChange']
      profileSettingsHandler.updateTagline(userName, taglineChange)
      return redirect(url_for('profileSettingsPage'))
    else:
      print(f'change tagline form invalid')

    if changeContentForm.validate_on_submit():
      print(f'change user content form valid')
      newContent = request.form['newContent']
      profileSettingsHandler.updateUserContent(userName, newContent)
      return redirect(url_for('profileSettingsPage'))
    else:
      print(f'change content form invalid')

    return render_template('profile_settings.html', 
    userInfo=userInfo, 
    userAccessInfo=userAccessInfo, 
    changeAvatarForm=changeAvatarForm,
    changePasswordForm=changePasswordForm,
    changeTaglineForm=changeTaglineForm,
    changeContentForm=changeContentForm)

#community page routing
@app.route('/communityPage', methods=['GET', 'POST'])
def communityPage():
  if request.method == 'POST':
    return redirect(url_for('feed'))
  sortPostForm = SortPostForm()
  replyForm = ReplyForm()
  makePostForm = MakePostForm()
  communityInfo = Community.query.filter_by(community_id = 2).first()
  posts = Post.query.all()
  print(posts)
  return render_template('community_page.html', makePostForm=makePostForm, sortPostForm=sortPostForm, replyForm=replyForm, posts=posts, communityInfo=communityInfo)


@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('login'))