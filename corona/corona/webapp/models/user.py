# -*- coding: utf-8 -*-



from mongoengine import *

import datetime

class User(Document):

    user_name = StringField()
    user_password = StringField()
    title = StringField(default='looper')
    weight = IntField(default=1)
