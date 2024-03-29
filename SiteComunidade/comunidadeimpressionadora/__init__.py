from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy

app = Flask(__name__, template_folder='templates/')

app.config['SECRET_KEY'] = 'fe7d7f6bde3b0ec4e090e64b6384caf1'
if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
if not engine.has_table("usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("Base de dados criada")
else:
    print("Base de dados já existente")

from comunidadeimpressionadora import routes