from flask import Flask, render_template, flash, redirect, url_for, request
from LoginForm import LoginForm
from Change_Password_Form import ChangePasswordForm
from Logout_Form import LogoutForm
from datetime import datetime, timedelta
from Logger import Logger
from Log_Analyzer import Log_Analyzer


app = Flask(__name__)

#randomly generated secret key I may use for something later
app.config['SECRET_KEY'] = '31271d66321b32a7f3e9ad4c27106e85'

#global constants
COMMON_PASSWORD_FILE = 'CommonPassword.txt'
STATIC_CREDENTIALS_FILE = 'credentials.txt'

#global variables
validLogin = True
validUserName = ''
invalidAttemptCount = 0
#placeholder is a date time ovject
lockDate = datetime
onHold = False


def validateLogin(usernameToCheck, passwordToCheck):
    global validUserName

    with open(STATIC_CREDENTIALS_FILE, 'r') as credentialsFile:
        fileText = []
        for line in credentialsFile:
            fileText.append(line)
        username = fileText[0].strip()
        password = fileText[1].strip()
        if (username == usernameToCheck and password == passwordToCheck):
            validUserName = username
            return True
        else:
            return False

def isCommonPassword(inputPassword):
    passwordIsCommon = False
    with open(COMMON_PASSWORD_FILE, 'r') as passwordFile:
        commonPasswords = []
        for line in passwordFile:
            strippedLine = line.strip()
            commonPasswords.append(strippedLine)
        for password in commonPasswords:
            if (password == inputPassword):
                passwordIsCommon = True
    return passwordIsCommon
            

def updatePassword(passwordToWrite):
    global validUserName

    with open(STATIC_CREDENTIALS_FILE, 'w', newline='\n') as credentialsFile:
        #write username
        credentialsFile.write(validUserName + '\n')
        #write password
        credentialsFile.write(passwordToWrite)


#index
@app.route('/', methods=['GET', 'POST'])
def index():
    global validLogin
    global invalidAttemptCount
    global onHold
    global lockDate

    #instantiate forms
    form = LoginForm()
    logger = Logger()
  

    #form validation
    if form.validate_on_submit():
        #run log analysis
        analyzer = Log_Analyzer()
        analyzer.check_logs()

        currentTime = datetime.now()
        if ((onHold != True) or (onHold == True and currentTime >= lockDate)):
            if (validateLogin(form.username.data, form.password.data)):
                flash(f'You have successfully logged in as {form.username.data}', 'success')
                validLogin = True
                #redirect to login page and set logged in value
                #clear login counter
                invalidAttemptCount = 0
                return redirect(url_for('loggedin'))
            else:
                flash(f'Username and Password do not match', 'danger')
                # grab IP address and current date tiem
                ipAddress = request.environ['REMOTE_ADDR']
                if (invalidAttemptCount == 0):
                    #is first attempt
                    firstAttemptDateTime = datetime.now()
                invalidAttemptCount += 1
                #log the invalid attempt
                logger.log_invalid_attempt(ipAddress)
                if (invalidAttemptCount >= 15):
                    #over 15 attempt
                    onHold = True
                    lockDate = datetime.now() + timedelta(minutes = 5)
        else:
            currentTime = datetime.now()
            dateDifference = lockDate - currentTime
            secondsRemaining = dateDifference.seconds
            minutesRemaining = secondsRemaining / 60
            flash(f'you have entered too many invalid attempts, please try again in {int(minutesRemaining) + 1} minutes', 'danger')
                  
    return render_template('index.html', form=form)

#loggind-in
@app.route('/logged-in', methods=['GET', 'POST'])
def loggedin():
    global validLogin

    form = ChangePasswordForm()
    logout_form = LogoutForm()

    if request.method == 'POST':
        #need to check the button action or something
        if 'logout' in request.form:
            validLogin = False
            return redirect(url_for('index'))

    if form.validate_on_submit():
        if (isCommonPassword(form.password.data)):
            flash(f'password is too common, try another password', 'danger')
        else:
            updatePassword(form.password.data)
            flash(f'You have succesfully updated your password', 'success')
        

    if (validLogin == False):
        #redirect
        return redirect(url_for('index'))
    else:
        return render_template('private.html', form = form, logout_form = logout_form)

#debugging
if __name__ == '__main__':
    app.run(debug=True)