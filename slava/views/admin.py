from slava import db
from flask import render_template
from flask.ext.login import login_required
from slava.authentication import admin_required


@login_required
@admin_required
def index():
  return "hi"
