from slava.views import core, profile
import slava.authentication as auth

routes = [
    ('/', core.index, ['GET']),
    ('/login/', auth.login_redirect, ['GET']),
    ('/login/error/', auth.login_error, ['GET']),
    ('/profile/', profile.profile, ['GET']),
    ('/profile/namechange/', profile.setname, ['POST']),
    ('/oauth2callback/', auth.oauth_callback, ['GET']),
    ('/test/', core.test_page, ['GET'])
]


def add_routes(app):
  for route, view_function, request_method in routes:
    app.add_url_rule(
        route,
        view_function.__name__,
        view_function,
        methods=request_method
    )
