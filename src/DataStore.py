#!/usr/bin/python3

class DataStore:
    def __init__(self, model, json_dump):
        self.data_structure = model
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


    def __verify_data_consistency(self):
        # TODO find a way to scan through and ensure no obvious issues in the info
        pass

    def __build_field_index_data_structure(self):
        data_structure = {}
        for field in self.data_structure.mandatory_fields:
            data_structure[field] = {}
        return data_structure


    def __index_by_id(self, id_index, data):
        id_to_index = str(data['_id'])
        if not id_to_index in id_index:
            id_index[id_to_index] = data
            return id_index
        else:
            # TODO error handling since duplicate user ID not permitted
            exit(1)


    def __index_by_field(self, field_index, data):
        for field in data:

            # Managing list fields
            if isinstance(data[field], list):
                for list_entry in data[field]:
                    if list_entry not in field_index[field]:
                        field_index[field][str(list_entry)] = [str(data['_id'])]
                    else:
                        field_index[field][str(list_entry)].append(str(data['_id']))

            # Managing other fields
            else:
                if data[field] in field_index[field]:
                    field_index[field][str(data[field])].append(str(data['_id']))
                else:
                    field_index[field][str(data[field])] = [str(data['_id'])]

        return field_index
