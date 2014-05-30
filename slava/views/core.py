from flask.ext.login import login_required
from flask import render_template, request


def index():
  return render_template('index.html')
