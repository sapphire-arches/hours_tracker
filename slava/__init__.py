import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from slava.routes import add_routes

app = Flask(__name__)

app.logger.log(level=9, msg=str(type(app.logger)))

# Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

# Routing
add_routes(app)
