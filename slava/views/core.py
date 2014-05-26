from flask.ext.login import login_required


def index():
  return "hello world"


def login():
  return "loggin in is fun =P"


@login_required
def test_page():
  return "you are logged in"
