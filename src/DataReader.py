#!/usr/bin/python3

import json

# TODO add error handling for bad json


class DataReader:
    def read_data(self, filename):
        with open(filename) as f:
            return json.loads(f.read())
