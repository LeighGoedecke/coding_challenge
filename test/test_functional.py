#!/usr/bin/python3

import unittest

from src.DataStore import DataStore
from src.SearchEngine import SearchEngine
from test.fixtures import *

class FunctionalTest(unittest.TestCase):
    def test_connect_data_store_with_search_engine(self):
        index = {'DummyModel': DataStore(DummyModel(), DUMMY_MODEL_DATA).index_data(),
                 'AnotherDummyModel': DataStore(AnotherDummyModel(), ANOTHER_DUMMY_MODEL_DATA).index_data()}
        search_params = {
            'model': AnotherDummyModel(),
            'search_key': '_id',
            'search_value': '22'
        }

        search_results = SearchEngine(index, search_params).search()
        self.assertEqual(search_results, {'primary_data': [{'_id': 22, '5sos': ['Ashton', 'Luke', 'Michael'], 'description': 'also_still_a_band', 'a_cool_band': True, 'friend_id': 2}], 'associated_field_data': [{'_id': 2, 'one_direction': ['Liam', 'Louis', 'Zayn'], 'description': 'still_a_band', 'cool_band': True, 'friend_id': 22}]})


if __name__ == '__main__':
    unittest.main()
