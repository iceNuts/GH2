# -*- coding: utf-8 -*-

from mongoengine import *

import datetime

class Attribute(Document):

    taxonomy = StringField()
    version = DateTimeField(default=datetime.datetime.now)
    data = StringField()
