def app(environ, start_response):
    """A barebones WSGI application.
    This is a starting point for your own Web framework :)
    """
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return 'Hello, %s!' % (environ['PATH_INFO'][1:] or 'web')
