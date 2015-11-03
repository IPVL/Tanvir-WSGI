#! /usr/bin/env python
class TestMiddle:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print "this works"
	for chunk in self.app(environ, start_response):
            yield chunk.lower()
