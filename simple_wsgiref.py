#! /usr/bin/env python

# Python's bundled WSGI server using wsgiref 
# wsgiref is a reference implementation of the WSGI specification that can be used to add WSGI support to a web server or framework.
from wsgiref.simple_server import make_server

def application (environ, start_response):

    # Sorting and stringifying the environment key, value pairs
    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return response_body

# Instantiate the server
httpd = make_server (
    '192.168.8.91', # The host name
    8080, # A port number where to wait for the request
    application # The application object name, in this case a function
)

# Wait for a single request, serve it and quit
print "Server running..."
httpd.handle_request()

