
from webapp.models import User
from webapp.models import Taxonomy
from webapp.models import Attribute

import logging
import json

def load():

    li = User(
        user_name='li',
        user_password='123',
        title='looper',
        weight=2
        )
    li.save()

    yi = User(
        user_name='yi',
        user_password='123',
        title='killer',
        weight=3       
        )
    yi.save()

    gongxia = User(
        user_name='gongxia',
        user_password='123',
        title='player',
        weight=1
        )
    gongxia.save()

    chuan = User(
        user_name='chuan',
        user_password='123',
        title='looper',
        weight=2
        )
    chuan.save()

    name_list_li = [
        'JSON',
        'HACK',
        'HUMAN',
        'RACE',
        'LOVE'
    ]

    name_list_yi = [
        'LIFE',
        'COMPUTER',
        'WASHU',
        'AAYA',
        'BIG BOY'
    ]

    like_list_li = [
        23,
        17,
        29,
        88,
        67
    ]

    like_list_yi = [
        55,
        13,
        10,
        7,
        91
    ]

    for num in xrange(5):
        filename = 'test_data/' + str(num) + '.json'
        data = load_data_from_json(filename)
        fake_taxonomy(data, str(li.id), 1, name_list_li, like_list_li, num)
        fake_taxonomy(data, str(yi.id), 0, name_list_yi, like_list_yi, num)


def load_data_from_json(filename):

    with open(filename) as json_file:
        json_data = json.load(json_file)

        return json_data

def fake_taxonomy(data, uid, private, name_list, like_list, num):

        taxonomy = Taxonomy(
            owner=uid,
            name=str(name_list[num]),
            private=private,
            like=like_list[num]
            )
        taxonomy.save()

        count_data = json.dumps(data['count'])
        tree_data = json.dumps(data['tree'])
        chain_data = json.dumps(data['chain'])

        attr_count = Attribute(
            taxonomy=str(taxonomy.id),
            data=count_data
            )
        attr_count.save()

        attr_tree = Attribute(
            taxonomy=str(taxonomy.id),
            data=tree_data
            )
        attr_tree.save()

        attr_chain = Attribute(
            taxonomy=str(taxonomy.id),
            data=chain_data
            )
        attr_chain.save() 












