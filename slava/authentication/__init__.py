from slava.models import User
from slava import app, db, login_manager
from flask import flash

@login_manager.user_loader
def load_user(userid):
  session = db.session
  return session.query(User).filter(User.name == userid)


def perform_login():
  app.logger.log(level=9, msg='hello world')
  flash('hello!')
  return "logged in"
