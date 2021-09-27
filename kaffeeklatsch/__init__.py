from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_files/application_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#randomly generated secret key I may use for something later
app.config['SECRET_KEY'] = '31271d66321b32a7f3e9ad4c27106e85'

db = SQLAlchemy(app)
Session(app)
login_manager = LoginManager(app)



from kaffeeklatsch import routes