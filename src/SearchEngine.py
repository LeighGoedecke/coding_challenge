#!/usr/bin/python3

class SearchEngine:
    def __init__(self, index, search_params):
        self.index = index
        self.search_params = search_params

    def search(self):
        # if search key is anything else then we go to our field_index to retrieve id (or ids)
        model = self.search_params['model']
        search_key = self.search_params['search_key']
        search_value = self.search_params['search_value']

        if self.search_params['search_key'] != '_id':
            discovered_ids = self.__search_field_index(model.name, search_key, search_value)
        else:
            discovered_ids = search_value

        if not isinstance(discovered_ids, list):
            discovered_ids = [discovered_ids]

        associated_ids = [self.__search_id_index(model.name, some_id) for some_id in discovered_ids]

        shared_field_ids = []
        if model.shared_fields and associated_ids:
            shared_field_ids = self.__search_shared_field_info(model.shared_fields, associated_ids)

        return {
            'primary_data': associated_ids,
            'shared_field_data': shared_field_ids
        }

    def __search_field_index(self, model_name, search_key, search_value):
        if search_value in self.index[model_name]['field_index'][search_key]:
            return self.index[model_name]['field_index'][search_key][search_value]

    def __search_id_index(self, model_name, id_to_search):
        if id_to_search in self.index[model_name]['id_index']:
            return self.index[model_name]['id_index'][id_to_search]

    def __search_shared_field_info(self, shared_fields, associated_ids):
        shared_field_id_lookup = []
        for shared_field in shared_fields:
            for id_data in associated_ids:
                if id_data:
                    if shared_field in id_data:
                        shared_id = str(id_data[shared_field])
                        shared_field_id_lookup.append(self.__search_id_index(shared_fields[shared_field], shared_id))
        return shared_field_id_lookup

