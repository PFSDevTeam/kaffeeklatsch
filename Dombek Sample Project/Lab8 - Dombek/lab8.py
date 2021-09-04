# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10
@author: rdombek
"""
import time
import re
from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)
app.secret_key = "mySuperSecretKey"
app.database = "sample.db"
@app.route('/home')
def home():
    """ method for homepage"""
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    """method for login"""
    if request.method == 'POST':
        updatepassword = request.form.get('update')
        # if checkbox is selected it will go to update page
        if updatepassword == 'true':
            return redirect(url_for('update'))
        username = request.form['username']
        password = request.form['password']
        # opens text file in read mode
        data = open('data.txt', 'r')
        while True:
            error = 0
            tortillas = data.readline()
            tortillas = tortillas.split(', ')
            name = tortillas[0]
            loginpass = tortillas[1]
            # if username exists and password matches this logs in and goes to homepage
            if username in name:
                if loginpass.strip() == password.strip():
                    data.close()
                    session['logged_in'] = True
                    flash('Thank you for logging in.')
                    return redirect(url_for('home'))
                # if no match then send error and goes back to login
                # also if no match sends username, data/time, and IP address of user to log.txt
                error = 'true'
                if error:
                    addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
                    print(addr)
                    dstr = time.strftime('%c')
                    print(dstr)
                    log = open('log.txt', 'a')
                    log.write('\n' + username + ', ' + dstr + ', ' + addr)
                feedback = 'Password and Username do not match.'
                data.close()
                return render_template('login.html', feedback=feedback)
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """register method"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # check to see if the password is in the common password file
        filename = 'CommonPassword.txt'
        with open(filename) as f_obj:
            common_password_list = f_obj.read()
        # if it is in common password list send message and go back to register
        if password in common_password_list:
            feedback = 'Please select a different secret password.'
            return render_template('register.html', feedback=feedback)
        #***** information for this taken from geaksforgeaks.org *****#
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{12,25}$"
        # compiling regex
        pat = re.compile(reg)
        # searching regex
        mat = re.search(pat, password)
        # validating conditions
        if mat:
            data = open('data.txt', 'a')
            data.write('\n' + username + ', ' + password)
            data.close()
            flash('Thank you for registering.')
            return redirect(url_for('login'))
        else:
            feedback = 'Password must be at least 12 characters, 1 Capital, 1 lower,\
                1 number, and 1 special'
            return render_template('register.html', feedback=feedback)
    return render_template('register.html')

@app.route('/update', methods=['GET', 'POST'])
def update():
    """update method"""
    if request.method == 'POST':
        username = request.form['username']
        oldpassword = request.form['oldpassword']
        newpassword = request.form['newpassword']
        password = newpassword
        with open('data.txt', 'r') as f:
            data = f.readlines()
        with open('data.txt', 'w') as f:
            for line in data:
                if line.strip('\n') != username + ", " + oldpassword:
                    f.write(line)
        filename = 'CommonPassword.txt'
        with open(filename) as f_obj:
            common_password_list = f_obj.read()
        if password in common_password_list:
            feedback = 'Please select a different secret password.'
            return render_template('update.html', feedback=feedback)
        #***** information for this taken from geaksforgeaks.org *****#
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{12,25}$"
        # compiling regex
        pat = re.compile(reg)
        # searching regex
        mat = re.search(pat, password)
        # validating conditions
        if mat:
            data = open('data.txt', 'a')
            data.write('\n' + username + ', ' + password)
            data.close()
            flash('You have successfully updated your password!')
            return redirect(url_for('login'))
        else:
            feedback = 'Password must be at least 12 characters, 1 Capital, 1 lower,\
                1 number, and 1 special'
            return render_template('update.html', feedback=feedback)
    return render_template('update.html')

@app.route('/logout')
def logout():
    """logout method"""
    session.pop('logged_in', None)
    flash('You have successfully logged out!')
    return redirect(url_for('login'))

@app.route('/pagetwo')
def biomed():
    """method for second page"""
    return render_template('pagetwo.html')

@app.route('/pagethree')
def general():
    """method for third page"""
    return render_template('pagethree.html')

if __name__ == '__main__':
    app.run(debug=True)
