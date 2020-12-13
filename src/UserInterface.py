#!/usr/bin/python3

class UserInterface:
    def __init__(self, data_sources):
        self.data_sources = data_sources
        self.table_mapping = {
            '1': 'Users',
            '2': 'Tickets',
            '3': 'Organizations'
        }

    def display_search_options(self):
        print('Please choose from options \'1\', \'2\' or type \'quit\'')

    def retrieve_search_option(self):
        print('\n\tSelect search options:')
        print('\t* Press 1 to search Zendesk')
        print('\t* Press 2 to view a list of searchable fields')
        return input('\t* Type \'quit\' to exit\n')

    def exit_search_app(self):
        print('Thank you for using Zendesk Search!')
        exit()

    def display_intro(self):
        print('Welcome to Zendesk Search')
        initial_selection = input(
            'Type \'quit\' at any time to exit. Press \'Enter\' to continue. ')
        if initial_selection == 'quit':
            self.exit_search_app()

    def retrieve_searchable_fields(self):
        searchable_fields = {}
        for source in self.data_sources:
            searchable_fields[source] = self.data_sources[source]['model']
        return searchable_fields

    def display_all_searchable_fields(self, searchable_fields):
        for category in searchable_fields:
            print(f'Search {category} with:')
            self.__print_underline()
            for field in searchable_fields[category].possible_fields:
                print(field)
            self.__print_delimiter()
        print('\n')

    def display_search_data(self, search_results):
        if not search_results['primary_data']:
            print('No results found')
            return
        print('Primary search results:')
        self.__print_underline()
        for search_result in search_results['primary_data']:
            self.__dict_printer(search_result)
        if search_results['associated_field_data']:
            print('\nAssociated search data:')
            self.__print_underline()
            for result in search_results['associated_field_data']:
                self.__dict_printer(result)

    def display_error(self, error):
        print(error)
        self.exit_search_app()

    def retrieve_search_params(self):
        searchable_fields = self.retrieve_searchable_fields()
        table_selection = input(
            'Select 1) Users, 2) Tickets, or 3) Organizations\n')
        if table_selection not in ['1', '2', '3', 'quit']:
            print('Please choose one of the available options 1, 2, 3 or type \'quit\' to exit')
            return
        elif table_selection == 'quit':
            self.exit_search_app()
        else:
            search_key_input = input('Enter search key: ')

        if search_key_input in searchable_fields[self.table_mapping[table_selection]].possible_fields:
            search_value = input('Enter search value: ')
            # necessary since python boolean is uppercase
            if search_value == 'true' or search_value == 'false':
                search_value = search_value.capitalize()
            print(f'\nSearching {search_key_input} for {search_value}\n')
            return {
                'model': self.data_sources[self.table_mapping[table_selection]]['model'],
                'search_key': search_key_input,
                'search_value': search_value
            }
        else:
            print(f'\nSorry {search_key_input} is not a valid search key')
            print('The available search fields for your selection are as follows:\n')
            for field in searchable_fields[self.table_mapping[table_selection]].possible_fields:
                print(field)

    def __lists_to_strings(self, dict_to_print):
        tidy_dict = {}
        for item in dict_to_print:
            if isinstance(dict_to_print[item], list):
                dict_to_print[item] = ', '.join(dict_to_print[item])

            value_to_clean = str(dict_to_print[item])
            if len(value_to_clean) > 40:
                tidy_dict[item] = str(value_to_clean)[:40] + '...'
            else:
                tidy_dict[item] = str(value_to_clean)
        return tidy_dict

    def __dict_printer(self, dict_to_print):
        cleaned_dict = self.__lists_to_strings(dict_to_print)
        [print('{:<25} {:>45}'.format(key, value)) for key, value in cleaned_dict.items()]
        self.__print_delimiter()

    def __print_underline(self):
        print('-----------------------------------------------------------------------')

    def __print_delimiter(self):
        print('                        ----------------------                        ')

