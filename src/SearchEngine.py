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
            discovered_id = self.index[model.name]['field_index'][search_key][search_value]
        else:
            discovered_id = search_value

        # Do id lookup
        info_associated_with_id = []
        if isinstance(discovered_id, list):
            for some_id in discovered_id:
                info_associated_with_id.append(self.search_by_id(model.name, some_id))
        else:
            info_associated_with_id = [self.search_by_id(model.name, discovered_id)]

        shared_field_info = []
        if model.shared_fields:
            for shared_field in model.shared_fields:
                for info in info_associated_with_id:
                    if shared_field in info:
                        shared_id = str(info[shared_field])
                        shared_field_info.append(self.search_by_id(model.shared_fields[shared_field], shared_id))

        print(info_associated_with_id)
        print(shared_field_info)

    def search_by_id(self, model_name, id_to_search):
        if id_to_search in self.index[model_name]['id_index']:
            return self.index[model_name]['id_index'][id_to_search]

    def display_search_results(self):
        pass

