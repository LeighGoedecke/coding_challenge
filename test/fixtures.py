#!/usr/bin/python3

class DummyModel:
    def __init__(self):
        self.name = 'DummyModel'
        self.possible_fields = ['_id', 'one_direction', 'description', 'cool_band', 'friend_id']
        self.associated_fields = {
            'AnotherDummyModel': {
                '_id': ['friend_id']
            }
        }

class AnotherDummyModel:
    def __init__(self):
        self.name = 'AnotherDummyModel'
        self.possible_fields = ['_id', '5sos', 'description', 'a_cool_band', 'friend_id']
        self.associated_fields = {
            'DummyModel': {
                '_id': ['friend_id']
            }
        }


DUMMY_MODEL_DATA = [{
    '_id': 1,
    'one_direction': ['Zayn', 'Harry', 'Liam'],
    'description': 'some_band',
    'cool_band': True,
    'friend_id': 22
},
    {
        '_id': 2,
        'one_direction': ['Liam', 'Louis', 'Zayn'],
        'description': 'still_a_band',
        'cool_band': True,
        'friend_id': 22
    }
]

BAD_FIELD_DUMMY_MODEL_DATA = [{
    '_id': 1,
    'one_direction': ['Zayn', 'Harry', 'Liam'],
    'best_band_ever': True,
    'description': 'some_band',
    'cool_band': True,
    'friend_id': 22
},
    {
        '_id': 2,
        'one_direction': ['Liam', 'Louis', 'Zayn'],
        'description': 'still_a_band',
        'cool_band': True,
        'friend_id': 22
    }
]

DUPLICATE_ID_DUMMY_MODEL_DATA = [{
    '_id': 1,
    'one_direction': ['Zayn', 'Harry', 'Liam'],
    'best_band_ever': True,
    'description': 'some_band',
    'cool_band': True,
    'friend_id': 22
},
    {
        '_id': 1,
        'one_direction': ['Liam', 'Louis', 'Zayn'],
        'description': 'still_a_band',
        'cool_band': True,
        'friend_id': 22
    }
]

NO_ID_DUMMY_MODEL_DATA = [{
    'one_direction': ['Zayn', 'Harry', 'Liam'],
    'description': 'some_band',
    'cool_band': True,
    'friend_id': 22
},
    {
        '_id': 2,
        'one_direction': ['Liam', 'Louis', 'Zayn'],
        'description': 'still_a_band',
        'cool_band': True,
        'friend_id': 22
    }
]


ANOTHER_DUMMY_MODEL_DATA = [{
    '_id': 11,
    '5sos': ['Luke', 'Calum', 'Michael'],
    'description': 'also_some_band',
    'a_cool_band': True,
    'friend_id': 1
},
    {
        '_id': 22,
        '5sos': ['Ashton', 'Luke', 'Michael'],
        'description': 'also_still_a_band',
        'a_cool_band': True,
        'friend_id': 2
    }
]