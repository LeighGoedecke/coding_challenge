#!/usr/bin/python3

import json

def data_reader(filename):
    with open(filename) as f:
        return json.loads(f.read())



# with open(f'resources/users.json') as f:
#     user_data = json.loads(f.read())
# user_structure = Users()
# User = DataStore(user_structure, user_data)
# print(User.indexed_by_field["url"])

