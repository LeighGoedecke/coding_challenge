#!/usr/bin/python3

import json
from Users import Users


class DataStore:
    def __init__(self, data_structure, json_dump):
        self.data_structure = data_structure
        self.json_dump = json_dump
        self.indexed_by_id = self.__index_by_id()
        self.indexed_by_field = self.__index_by_field()

    def __verify_data_consistency(self):
        pass

    def __build_field_index_data_structure(self):
        data_structure = {}
        for field in self.data_structure.mandatory_fields:
            data_structure[field] = {}
        return data_structure

    def __index_by_id(self):
        id_index = {}
        for data in self.json_dump:
            if not data['_id'] in id_index:
                id_index[data['_id']] = data
            else:
                # TODO error handling since duplicate user ID not permitted
                continue
        return id_index

    def __index_by_field(self):
        field_index = self.__build_field_index_data_structure()
        for data in self.json_dump:
            for field in data:

                # Managing list fields
                if isinstance(data[field], list):
                    for list_entry in data[field]:
                        if list_entry not in field_index['tags']:
                            field_index['tags'][list_entry] = [data['_id']]
                        else:
                            field_index['tags'][list_entry].append(data['_id'])

                # Managing other fields
                else:
                    if data[field] in field_index[field]:
                        field_index[field][data[field]].append(data['_id'])
                    else:
                        field_index[field][data[field]] = [data['_id']]

        return field_index


with open(f'resources/users.json') as f:
    user_data = json.loads(f.read())
user_structure = Users()
User = DataStore(user_structure, user_data)
print(User.indexed_by_field["url"])
