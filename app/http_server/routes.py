from app.http_server.views.views import HelloView

routes = [
    ('GET', r'/hello', HelloView, 'version'),
]
