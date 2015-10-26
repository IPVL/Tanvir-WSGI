#! /usr/bin/env python

# this is a simple function of WSGI using Paste package

success = "You are authorized :D\n"
wrong = "Sorry Try Again\n"


def verify(user_name, password):
    if user_name == "pantho" and password == "1234":
        return success
    else:
        return wrong


def app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    user_name = environ['HTTP_USERNAME']
    password = environ['HTTP_PASSWORD']
    result = verify(user_name, password)
    return result
