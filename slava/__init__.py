import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.debug = True

login_manager = LoginManager()
login_manager.init_app(app)

app.logger.log(level=9, msg=str(type(app.logger)))

# Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
app.secret_key = os.environ['SECRET_KEY']

# Routing
# everything must be initialized before we can import the routes module
from slava.routes import add_routes
add_routes(app)
