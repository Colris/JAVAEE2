    #!bash
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response(
        'Hello world from Pyramid!\n',
        content_type='text/plain',
    )

config = Configurator()
config.add_route('hello.html', '/hello.html')
config.add_view(hello_world, route_name='hello.html')
app = config.make_wsgi_app()