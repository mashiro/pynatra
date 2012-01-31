#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pynatra.base import Base

class Application(Base):
    pass

# Classic Style
application = Application()
get = application.get
post = application.post

import atexit
@atexit.register
def start_server():
    from wsgiref.simple_server import make_server
    print 'Start server: locahost:8080'
    server = make_server('127.0.0.1', 8080, application)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

__all__ = ['get', 'post']
