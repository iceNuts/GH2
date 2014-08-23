# -*- coding: utf-8 -*-

from mongoengine import *

import datetime


class Taxonomy(Document):

    owner = StringField()
    name = StringField(default='Awesome Taxonomy')
    update_time = DateTimeField(default=datetime.datetime.now)
    like = IntField(default=0)
    private = IntField(default=1) # 0 public

    meta = {
            'indexes': 
            [
                {
                'fields': [
                        'owner',
                        'name', 
                        'update_time', 
                        'private',
                        '-like',
                    ]
                }
            ]
        }