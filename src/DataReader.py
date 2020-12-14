#!/usr/bin/python3

import json

class DataReader:
    def read_data(self, filename):
        try:
            with open(filename) as f:
                return json.loads(f.read())
        except (json.decoder.JSONDecodeError, FileNotFoundError) as e:
            raise e
