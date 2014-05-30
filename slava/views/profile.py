from flask.ext.login import login_required, current_user
from flask import render_template, request, redirect
from slava import db, app


@login_required
def profile():
  return render_template('profile.html', uname=current_user.name)


@login_required
def setname():
  set_name = request.form.get('name')
  if set_name is not None and not(set_name == ''):
    current_user.name = set_name
    db.session.commit()
  return redirect('/profile/')
