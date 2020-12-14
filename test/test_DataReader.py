#!/usr/bin/python3

import unittest
import unittest.mock as um
import json

from src.DataReader import DataReader


class TestDataReader(unittest.TestCase):
    def test_read_well_formed_json(self):
        well_formed_json = json.dumps({
            'test': 123,
        })

        with um.patch('builtins.open', um.mock_open(read_data=well_formed_json)):
            data_reader = DataReader()
            fake_data = data_reader.read_data('file/path')
            self.assertEqual(fake_data, {'test': 123})

    def test_read_poorly_formed_json_throws_error(self):
        not_json = 'definitely_not_json'

        with um.patch('builtins.open', um.mock_open(read_data=not_json)):
            with self.assertRaises(json.decoder.JSONDecodeError):
                data_reader = DataReader()
                data_reader.read_data('file/path')


if __name__ == '__main__':
    unittest.main()
