
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

    name_list = [
        'JSON',
        'HACK',
        'HUMAN',
        'RACE',
        'LOVE',
        'LIFE',
        'COMPUTER',
        'WASHU'
    ]

    for num in xrange(8):
        filename = 'test_data/' + str(num) + '.json'
        data = load_data_from_json(filename)

        taxonomy = Taxonomy(
            owner=str(li.id),
            name=str(name_list[num]),
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


def load_data_from_json(filename):

    with open(filename) as json_file:
        json_data = json.load(json_file)

        return json_data














