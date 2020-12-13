#!/usr/bin/python3

import unittest
from src.SearchEngine import SearchEngine
from test.test_config import *

ANOTHER_DUMMY_MODEL_INDEX = {'id_index': {'11': {'_id': 11, '5sos': ['Luke', 'Calum', 'Michael'], 'description': 'also_some_band', 'a_cool_band': True, 'friend_id': 1}, '22': {'_id': 22, '5sos': ['Ashton', 'Luke', 'Michael'], 'description': 'also_still_a_band', 'a_cool_band': True, 'friend_id': 2}}, 'field_index': {'_id': {'11': ['11'], '22': ['22']}, '5sos': {'Luke': ['11', '22'], 'Calum': ['11'], 'Michael': ['11', '22'], 'Ashton': ['22']}, 'description': {'also_some_band': ['11'], 'also_still_a_band': ['22']}, 'a_cool_band': {'True': ['11', '22']}, 'friend_id': {'1': ['11'], '2': ['22']}}}
DUMMY_MODEL_INDEX = {'id_index': {'1': {'_id': 1, 'one_direction': ['Zayn', 'Harry', 'Liam'], 'description': 'some_band', 'cool_band': True, 'friend_id': 22}, '2': {'_id': 2, 'one_direction': ['Liam', 'Louis', 'Zayn'], 'description': 'still_a_band', 'cool_band': True, 'friend_id': 22}}, 'field_index': {'_id': {'1': ['1'], '2': ['2']}, 'one_direction': {'Zayn': ['1', '2'], 'Harry': ['1'], 'Liam': ['1', '2'], 'Louis': ['2']}, 'description': {'some_band': ['1'], 'still_a_band': ['2']}, 'cool_band': {'True': ['1', '2']}, 'friend_id': {'22': ['1', '2']}}}


INDEX = {
    "DummyModel": DUMMY_MODEL_INDEX,
    "AnotherDummyModel": ANOTHER_DUMMY_MODEL_INDEX
}

class TestSearchEngine(unittest.TestCase):
    def test_successful_search_by_id(self):
        existing_id = '2'

        search_params = {
            'model': DummyModel(),
            'search_key': '_id',
            'search_value': existing_id
        }
        search_result = SearchEngine(INDEX, search_params).search()
        assert search_result == {'primary_data': [{'_id': 2, 'one_direction': ['Liam', 'Louis', 'Zayn'], 'description': 'still_a_band', 'cool_band': True, 'friend_id': 22}], 'shared_field_data': [{'_id': 22, '5sos': ['Ashton', 'Luke', 'Michael'], 'description': 'also_still_a_band', 'a_cool_band': True, 'friend_id': 2}]}

    def test_null_search_by_id(self):
        not_existing_id = '3'

        search_params = {
            'model': DummyModel(),
            'search_key': '_id',
            'search_value': not_existing_id
        }
        search_result = SearchEngine(INDEX, search_params).search()
        assert search_result == {'primary_data': [], 'shared_field_data': []}


    def test_successful_search_by_field(self):
        existing_field = 'description'
        existing_value = 'also_some_band'

        search_params = {
            'model': AnotherDummyModel(),
            'search_key': existing_field,
            'search_value': existing_value
        }
        search_result = SearchEngine(INDEX, search_params).search()
        assert search_result == {'primary_data': [{'_id': 11, '5sos': ['Luke', 'Calum', 'Michael'], 'description': 'also_some_band', 'a_cool_band': True, 'friend_id': 1}], 'shared_field_data': [{'_id': 1, 'one_direction': ['Zayn', 'Harry', 'Liam'], 'description': 'some_band', 'cool_band': True, 'friend_id': 22}]}


    def test_null_search_by_field(self):
        existing_field = 'description'
        not_existing_value = 'shrek2'

        search_params = {
            'model': AnotherDummyModel(),
            'search_key': existing_field,
            'search_value': not_existing_value
        }
        search_result = SearchEngine(INDEX, search_params).search()
        assert search_result == {'primary_data': [], 'shared_field_data': []}

    def test_search_by_list_field(self):
        list_field = '5sos'
        existing_value = 'Calum'

        search_params = {
            'model': AnotherDummyModel(),
            'search_key': list_field,
            'search_value': existing_value
        }
        search_result = SearchEngine(INDEX, search_params).search()
        assert search_result == {'primary_data': [{'_id': 11, '5sos': ['Luke', 'Calum', 'Michael'], 'description': 'also_some_band', 'a_cool_band': True, 'friend_id': 1}], 'shared_field_data': [{'_id': 1, 'one_direction': ['Zayn', 'Harry', 'Liam'], 'description': 'some_band', 'cool_band': True, 'friend_id': 22}]}


if __name__ == '__main__':
    unittest.main()