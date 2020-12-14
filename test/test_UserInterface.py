#!/usr/bin/python3

import unittest
from src.UserInterface import UserInterface
from fixtures import *
from unittest.mock import patch

DATA_SOURCES = {
    "DUMMY_MODELS": {
        "source": "dummy/models.json",
        "model": DummyModel()
    }
}
#TODO add tests for other UI methods

class TestUserInterface(unittest.TestCase):
    @patch('builtins.print')
    def test_display_search_options(self, mock_print):
        UserInterface(DATA_SOURCES).display_search_options()
        mock_print.assert_called_with('Please choose from options \'1\', \'2\' or type \'quit\'')


if __name__ == '__main__':
    unittest.main()
