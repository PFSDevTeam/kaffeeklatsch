from flask import Flask, render_template, flash, redirect, url_for, request

app = Flask(__name__)

##FLASK APP HELLO WORLD

@app.route("/")
def hello():
  return render_template('index.html')

if __name__ == "__main__":
  app.run()