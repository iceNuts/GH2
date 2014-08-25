# -*- coding: utf-8 -*-

from mongoengine import *

import datetime

class Attribute(Document):

    taxonomy = StringField()
    attrtype = IntField() # 0 count 1 tree 2 chain
    version = DateTimeField(default=datetime.datetime.now)
    data = StringField()
