#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import wsgiref
import wsgiref.util

class Base(object):
    def __init__(self):
        self.maps = []

    def get(self, path, callback):
        self._root('GET', path, callback)

    def post(self, path, callback):
        self._root('POST', path, callback)

    def _root(self, method, path, callback):
        self.maps.append((method, path, callback))

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']

        body = None
        for map in self.maps:
            if map[0] == method and re.match(map[1], path):
                body = map[2]()

        if body is None:
            start_response('404 Not Found', [('Content-Type', 'text/plain')])
            return "404 Not Found"
        else:
            start_response('200 OK', [('Content-Type', 'text/plain')])
            return body

