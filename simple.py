#! /usr/bin/env python

# this is a simple application of WSGI using Paste package


if __name__ == '__main__':
    from paste import httpserver
    from simple_app import app
    from authentication import AuthVerification

    httpserver.serve(AuthVerification(app), host='192.168.8.91', port='8080')

# To run this app using terminal type : python simple.py

# Request 1 from terminal : curl -H "username":"tanvir" -H "password":"1234" -X GET 192.168.8.91:8080
# Output of this request: sorry try again

# Request 2 from  terminal : curl -H "username":"tanvir" -H "password":"ahmed" -X GET 192.168.8.91:8080
# Output of this request: sorry try again

# Request 3 from  terminal : curl -H "username":"pantho" -H "password":"1234" -X GET 192.168.8.91:8080
# Output of this request: you are authorized :d