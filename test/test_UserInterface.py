#!/usr/bin/python3

import unittest
from unittest.mock import patch

from src.UserInterface import UserInterface
from test.fixtures import *

DATA_SOURCES = {
    "DUMMY_MODELS": {
        "source": "dummy/models.json",
        "model": DummyModel()
    }
}

class TestUserInterface(unittest.TestCase):
    @patch('builtins.print')
    def test_display_search_options(self, mock_print):
        UserInterface(DATA_SOURCES).display_search_options()
        mock_print.assert_called_with('Please choose from options \'1\', \'2\' or type \'quit\'')

    @patch('builtins.print')
    def test_exit_search_app(self, mock_print):
        with self.assertRaises(SystemExit):
            UserInterface(DATA_SOURCES).exit_search_app()
        mock_print.assert_called_with('Thank you for using Zendesk Search!')

if __name__ == '__main__':
    unittest.main()
