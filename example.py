#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pynatra import *

get(r'^/$', (lambda:
    'Hello World!'
))

get(r'^/test$', (lambda:
    'Test'
))
