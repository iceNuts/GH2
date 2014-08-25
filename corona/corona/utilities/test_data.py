
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
        'JSON IS COOL',
        'HACK IN THE HOLE',
        'HUMAN IS INT',
        'RACE AGAINST PIG',
        'LOVE IS FOOLISH'
    ]

    name_list_yi = [
        'LIFE IS COOL',
        'COMPUTER IS - -',
        'WE LOVE WASHU',
        'AAYA IS we TEAM',
        'BIG BOY BIG DREAM'
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

    private_list_li = [
        0,
        1,
        1,
        0,
        1
    ]

    private_list_yi = [
        0,
        0,
        0,
        0,
        0
    ]

    for num in xrange(5):
        filename = 'test_data/' + str(num) + '.json'
        data = load_data_from_json(filename)
        fake_taxonomy(data, str(li.id), private_list_li, name_list_li, like_list_li, num)
        fake_taxonomy(data, str(yi.id), private_list_yi, name_list_yi, like_list_yi, num)


def load_data_from_json(filename):

    with open(filename) as json_file:
        json_data = json.load(json_file)

        return json_data

def fake_taxonomy(data, uid, private_list, name_list, like_list, num):

        taxonomy = Taxonomy(
            owner=uid,
            name=str(name_list[num]),
            private=private_list[num],
            like=like_list[num]
            )
        taxonomy.save()

        count_data = json.dumps(data['count'])
        tree_data = json.dumps(data['tree'])
        chain_data = json.dumps(data['chain'])

        attr_count = Attribute(
            taxonomy=str(taxonomy.id),
            attrtype=0,
            data=count_data
            )
        attr_count.save()

        attr_tree = Attribute(
            taxonomy=str(taxonomy.id),
            attrtype=1,
            data=tree_data
            )
        attr_tree.save()

        attr_chain = Attribute(
            taxonomy=str(taxonomy.id),
            attrtype=2,
            data=chain_data
            )
        attr_chain.save() 












