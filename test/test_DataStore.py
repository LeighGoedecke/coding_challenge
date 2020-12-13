#!/usr/bin/python3

import unittest
from src.DataStore import DataStore
from test.test_config import *


class TestDataStore(unittest.TestCase):
    def test_index_data_has_correct_schema(self):
        data = DataStore(DummyModel(), DUMMY_MODEL_DATA)
        indexed_data = data.index_data()
        assert indexed_data == {'id_index': {'1': {'_id': 1, 'one_direction': ['Zayn', 'Harry', 'Liam'], 'description': 'some_band', 'cool_band': True, 'friend_id': 22}, '2': {'_id': 2, 'one_direction': ['Liam', 'Louis', 'Zayn'], 'description': 'still_a_band', 'cool_band': True, 'friend_id': 22}}, 'field_index': {'_id': {'1': ['1'], '2': ['2']}, 'one_direction': {'Zayn': ['1', '2'], 'Harry': ['1'], 'Liam': ['1', '2'], 'Louis': ['2']}, 'description': {'some_band': ['1'], 'still_a_band': ['2']}, 'cool_band': {'True': ['1', '2']}, 'friend_id': {'22': ['1', '2']}}}


if __name__ == '__main__':
    unittest.main()
