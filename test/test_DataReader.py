#!/usr/bin/python3

import unittest
import unittest.mock as um
from src.DataReader import DataReader
import json

# TODO test bad json error

class TestDataReader(unittest.TestCase):
    def test_read_data_successfully(self):
        well_formed_json = json.dumps({
            'test': 123,
        })

        with um.patch('builtins.open', um.mock_open(read_data=well_formed_json)):
            data_reader = DataReader()
            fake_data = data_reader.read_data('file/path')
            self.assertEqual(fake_data, {'test': 123})


if __name__ == '__main__':
    unittest.main()
