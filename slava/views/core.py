from flask.ext.login import login_required
from flask import render_template, request


def index():
  return render_template('index.html')


@login_required
def test_page():
  return "you are logged in"
