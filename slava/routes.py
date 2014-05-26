from slava.views import core

routes = [
    ('/', core.index, ['GET']),
    ('/login/', core.login, ['GET', 'POST']),
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
