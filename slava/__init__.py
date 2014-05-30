import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config['DEBUG'] = True

login_manager = LoginManager()

app.logger.log(level=9, msg=str(type(app.logger)))

# google config
app.config['GOOGLE_CLIENT_ID'] = os.environ['GOOGLE_CLIENT_ID']
app.config['GOOGLE_CLIENT_SECRET'] = os.environ['GOOGLE_CLIENT_SECRET']
app.config['GOOGLE_CALLBACK_URL'] = os.environ['GOOGLE_CALLBACK_URL']

# Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
app.secret_key = os.environ['SECRET_KEY']
login_manager.init_app(app)

# Routing
# everything must be initialized before we can import the routes module
from slava.routes import add_routes
add_routes(app)
