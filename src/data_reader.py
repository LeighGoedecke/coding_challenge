#!/usr/bin/python3

import json

def read_data(filename):
    with open(filename) as f:
        return json.loads(f.read())


