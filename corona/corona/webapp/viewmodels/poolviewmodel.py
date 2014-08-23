# -*- coding: utf-8 -*-

"""
    MVVM
    User View Model

"""

import logging
import datetime
import re
import hashlib

from webapp.models import Taxonomy
from webapp.models import Attribute

from datetime import datetime
from random import randint
from corona.settings import SECRET_KEY
from corona.settings import ACTIVATE_KEY


from django.core.exceptions import ValidationError
from django.core.cache import cache
from utilities import my_json

import logging


def popular_list_get():

    taxonomy = Taxonomy.objects(private=0)
    taxonomy_list = []
    for t in taxonomy:
        t = t.to_mongo()
        t = my_json.clean_bson(t)
        taxonomy_list.append(t)

    return taxonomy_list


def pool_list_get(uid):

    if not uid == None:
        taxonomy = Taxonomy.objects(owner=uid)
        taxonomy_list = []
        for t in taxonomy:
            t = t.to_mongo()
            t = my_json.clean_bson(t)
            taxonomy_list.append(t)

        return taxonomy_list
    else:
        raise ValidationError('invalid user')


def taxonomy_post(input):
    
    uid = input['uid']
    name = input['name']

    taxonomy = Taxonomy(
        owner=uid,
        name=name
        )
    taxonomy.save()


def taxonomy_get(object_id):

    if not object_id == None:
        taxonomy = Taxonomy.objects(pk=object_id).first()
        taxonomy = taxonomy.to_mongo()
        taxonomy = my_json.clean_bson(taxonomy)
        return taxonomy
    else:
        raise ValidationError('no such taxonomy')


def taxonomy_put(input):

    object_id = input['object_id']
    name = input['name']
    update_time = datetime.datetime.now

    taxonomy = Taxonomy.objects(pk=object_id)
    taxonomy.update(
        set__name=name,
        set__update_time=update_time,
        )

def taxonomy_delete(object_id):

    Taxonomy.objects(pk=object_id).delete


def like_taxonomy(input):

    object_id = input['object_id']
    taxonomy = Taxonomy.objects(pk=object_id)
    taxonomy.update(
        inc__like=1
        )


def publish_taxonomy(input):

    object_id = input['object_id']
    taxonomy = Taxonomy.objects(pk=object_id)
    taxonomy.update(
        set__private=0
        )


def attribute_post(input):

    taxonomy = input['taxonomy']
    meta = input['meta']

    attr = Attribute(
        taxonomy=taxonomy,
        meta=meta
        )
    attr.save()


def attribute_put(input):

    object_id = input['object_id']
    meta = input['meta']

    attr = Attribute.objects(pk=object_id)
    attr.update(
        set__meta=meta
        )

def attribute_get(taxonomy_id):

    attrs = Attribute.objects(taxonomy=taxonomy_id)
    attr_list = []
    for attr in attrs:
        attr = attr.to_mongo()
        attr = my_json.clean_bson(attr)
        attr_list.append(attr)
    return attr_list

def fork_taxonomy(input, userid):

    taxonomy_id = input['taxonomy_id']

    taxonomy = Taxonomy.objects(pk=taxonomy_id).first()

    new_taxonomy = Taxonomy(
        name=taxonomy.name
        )
    new_taxonomy.save()

    attrs = Attribute.objects(taxonomy=taxonomy_id)

    for attr in attrs:
        new_attr = Attribute(
            taxonomy=str(new_taxonomy.id),
            meta=attr.meta
            )
        new_attr.save()


def export_taxonomy(taxonomy_id):

    pass


def more_data_taxonomy(input):

    pass

























