#!/usr/bin/python3

from InvalidDataError import InvalidDataError

class DataStore:
    def __init__(self, model, json_dump):
        self.model = model
        self.json_dump = json_dump


    def index_data(self):
        id_index = {}
        field_index = self.__build_field_index_data_structure()
        for data in self.json_dump:
            id_index = self.__index_by_id(id_index, data)
            field_index = self.__index_by_field(field_index, data)
        return {
            'id_index': id_index,
            'field_index': field_index
        }


    def __build_field_index_data_structure(self):
        data_structure = {}
        for field in self.model.possible_fields:
            data_structure[field] = {}
        return data_structure


    def __index_by_id(self, id_index, data):
        if '_id' not in data:
            raise InvalidDataError(f"Data missing '_id' discovered within data set: {self.model.name}")

        id_to_index = str(data['_id'])
        if not id_to_index in id_index:
            id_index[id_to_index] = data
            return id_index
        else:
            raise InvalidDataError(f"Duplicate primary _id ({id_to_index}) discovered within data set: {self.model.name}")


    def __index_by_field(self, field_index, data):
        for field in data:
            if not field in self.model.possible_fields:
                raise InvalidDataError(f'Invalid data key ({field}) discovered in model: {self.model.name}')

            # Managing list fields
            if isinstance(data[field], list):
                for list_entry in data[field]:
                    if list_entry not in field_index[field]:
                        field_index[field][str(list_entry)] = [str(data['_id'])]
                    else:
                        field_index[field][str(list_entry)].append(str(data['_id']))

            # Managing other fields
            else:
                if str(data[field]) in field_index[field]:
                    field_index[field][str(data[field])].append(str(data['_id']))
                else:
                    field_index[field][str(data[field])] = [str(data['_id'])]

        return field_index
