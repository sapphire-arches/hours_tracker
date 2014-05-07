import sys
print(sys.path)
from slava.views import core

routes = [
    ('/', core.index)
    ]

def add_routes(app):
  for route, view_function in routes:
    app.add_url_rule(route, view_function.__name__, view_function, methods=['GET'])
