#! /usr/bin/env python

# this is a simple application of WSGI using Paste package


if __name__ == '__main__':
    from paste import httpserver
    from simple_app import app
    from authentication import AuthVerification

    httpserver.serve(AuthVerification(app), host='192.168.8.91', port='8080')

# To run this app using terminal type : python simplest.py
# Request from another terminal : curl 192.168.8.91:8080
# Output of this request: Welcome to hell using WSGI :D
