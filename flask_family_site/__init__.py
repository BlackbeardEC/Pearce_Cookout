## Import all the things
# 3rd Party
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
# Local
from flask_family_site.my_config import my_secret, my_user, my_password

## Config
app = Flask(__name__)
app.config['SECRET_KEY'] = my_secret
# SQLite because this app will never go over 100k hits/day
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = my_user
app.config['MAIL_PASSWORD'] = my_password
mail = Mail(app)

from flask_family_site import routes
