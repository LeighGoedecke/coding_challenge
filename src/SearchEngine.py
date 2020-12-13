#!/usr/bin/python3

class SearchEngine:
    def __init__(self, index, search_params):
        self.index = index
        self.search_params = search_params

    def search(self):
        model = self.search_params['model']
        search_key = self.search_params['search_key']
        search_value = self.search_params['search_value']

        # finding ids directly associated with search parameters
        if self.search_params['search_key'] != '_id':
            primary_ids = self.__search_field_index(
                model.name, search_key, search_value)
        else:
            primary_ids = search_value

        if not isinstance(primary_ids, list):
            primary_ids = [primary_ids]

        # searching id_index for full data set for each primary id
        primary_id_dicts = [self.__search_id_index(model.name,some_id) for some_id in primary_ids if self.__search_id_index(model.name,some_id)]

        # finding associated field data
        associated_field_dicts = []
        if model.associated_fields and primary_id_dicts:
            associated_field_dicts = self.__get_associated_records(
                model.associated_fields, primary_id_dicts)

        return {
            'primary_data': primary_id_dicts,
            'associated_field_data': associated_field_dicts
        }

    def __search_field_index(self, model_name, search_key, search_value):
        if search_value in self.index[model_name]['field_index'][search_key]:
            return self.index[model_name]['field_index'][search_key][search_value]

    def __search_id_index(self, model_name, id_to_search):
        if id_to_search in self.index[model_name]['id_index']:
            return self.index[model_name]['id_index'][id_to_search]

    def __get_associated_records(self, associated_fields, primary_id_dicts):
        associated_records = []
        for model in associated_fields:
            for associated_field in associated_fields[model]:
                associated_ids = []  # TODO extract into another method
                for primary_id in primary_id_dicts:
                    for field in associated_fields[model][associated_field]:
                        associated_id_discovery = self.__search_field_index(model, associated_field, str(primary_id[field]))
                        if associated_id_discovery:
                            associated_ids.extend(associated_id_discovery)
                        for found_id in associated_ids:
                            found_data = self.__search_id_index(model, found_id)
                            if found_data:
                                associated_records.append(found_data)
        return associated_records
