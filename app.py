from flask import Flask, render_template, flash, redirect, url_for, request

#ADDED FOR TESTING
from components.LoginHandler import LoginHandler

app = Flask(__name__)

##FLASK APP HELLO WORLD

@app.route("/")
def hello():
  #ADDED FOR TESTING
  loginHandler = LoginHandler("steve", "scuba")
  return render_template('index.html')

if __name__ == "__main__":
  app.run()