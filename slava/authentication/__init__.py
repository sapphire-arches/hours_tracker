from slava.models import User
from slava import app, db, login_manager
from flask import flash,redirect,request
from urllib.request import quote, urlopen, Request
from urllib.parse import urlencode
from urllib.error import HTTPError
import json

# temporary to generate random username
import string
import random


@login_manager.user_loader
def load_user(userid):
  session = db.session
  return session.query(User).filter(User.id == int(userid)).first()


def login_redirect():
  args = {
          'client_id':app.config['GOOGLE_CLIENT_ID'],
          'redirect_url':quote(app.config['GOOGLE_CALLBACK_URL']),
          'scope':quote('profile email') # we really only care if the user exists and has accepted our app
  }
  redirect_url = 'https://accounts.google.com/o/oauth2/auth?scope={scope}&redirect_uri={redirect_url}&client_id={client_id}&response_type=code'.format(**args)
  return redirect(redirect_url)

def _print_http_error(e, req):
  ed = {
      'url' : e.url,
      'errno' : e.code,
      'error' : e.reason,
      'headers' : e.hdrs,
      'request' : req,
      'request-headers' : req.header_items()
  }
  app.logger.warning('error {errno} : {error} posting to {url} with headers \n{headers}\nRequest headers were:\n{request-headers}'.format(**ed))

def _request(url, data=None):
  if data is not None:
    req = Request(url, data=urlencode(data).encode('iso-8859-1'))
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    try:
      return urlopen(req)
    except HTTPError as e:
      _print_http_error(e, req)
  else:
    try:
      req = Request(url, method='GET')
      return urlopen(req)
    except HTTPError as e:
      _print_http_error(e, req)

def _api_request(url, access_token):
  try:
    req = Request(url, method='GET')
    req.add_header('Authorization', 'Bearer {}'.format(access_token))
    return urlopen(req)
  except HTTPError as e:
    _print_http_error(e, req)

def oauth_callback():
  if 'error' in request.args:
    pass # not really much we can do here, TODO: display some feedback
  else:
    data = {
            'code' : request.args['code'],
            'client_id' : app.config['GOOGLE_CLIENT_ID'],
            'client_secret' : app.config['GOOGLE_CLIENT_SECRET'],
            'redirect_uri' : app.config['GOOGLE_CALLBACK_URL'],
            'grant_type' : 'authorization_code'
    }

    req = None

    # retrieve an access token
    req = _request('https://accounts.google.com/o/oauth2/token', data)
    result = json.loads(req.read().decode('iso-8859-1'))
    req.close()
    access_token = result['access_token']

    # get the user's email address
    req = _api_request('https://www.googleapis.com/plus/v1/people/me', access_token)
    result = json.loads(req.read().decode('iso-8859-1'))
    req.close()

    umail = result['emails'][0]['value']
    u = db.session.query(User).filter(User.email == umail).first()
    if u is None:
      uname = ''.join(random.choice(string.ascii_lowercase) for _ in range(12))
      u = User(uname, umail)
      db.session.add(u)
    u.access_token = access_token
    db.session.commit()
  return "hello {}, welcome to the hours tracker!".format(u.name)
