from flask.ext.login import LoginManager
from slava.models import User
from slava import app, db

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
  session = db.session
  return session.query(User).filter(User.name == userid)
