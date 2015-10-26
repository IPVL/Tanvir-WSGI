#! /usr/bin/env python

# this is a simple application of WSGI using Paste package
def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return ['Welcome to hell using WSGI! :D\n']

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(simple_app, host='192.168.8.91', port='8080')

# To run this app using terminal type : python simplest.py 
# Request from another terminal : curl 192.168.8.91:8080
# Output of this request: Welcome to hell using WSGI :D 
