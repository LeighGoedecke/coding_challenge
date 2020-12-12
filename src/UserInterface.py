#!/usr/bin/python3

import json

class UserInterface:
    def __init__(self, data_sources):
        self.data_sources = data_sources

    def display_search_options(self):
        print('Please choose from options \'1\', \'2\' or type \'quit\'')

    def retrieve_search_option(self):
        print('\tSelect search options:')
        print('\t* Press 1 to search Zendesk')
        print('\t* Press 2 to view a list of searchable fields')
        return input('\t* Type \'quit\' to exit\n')

    def exit_search_app(self):
        print('Thank you for using Zendesk Search!')
        exit()

    def display_intro(self):
        print('Welcome to Zendesk Search')
        initial_selection = input('Type \'quit\' at any time to exit. Press \'Enter\' to continue\n')
        if initial_selection == 'quit':
            self.exit_search_app()

    def retrieve_searchable_fields(self):
        searchable_fields = {}
        for source in self.data_sources:
            searchable_fields[source] = self.data_sources[source]['model']
        return searchable_fields

    def display_all_searchable_fields(self, searchable_fields):
        print(searchable_fields)
        for category in searchable_fields:
            print('----------------------------------')
            print(f'Search {category} with:')
            for field in searchable_fields[category].mandatory_fields:
                print(field)
        print('\n')


    def retrieve_search_params(self):
        searchable_fields = self.retrieve_searchable_fields()
        table_mapping = {
            '1': 'Users',
            '2': 'Tickets',
            '3': 'Organizations'
        }
        table_selection = input('Select 1) Users, 2) Tickets, or 3) Organizations\n')
        if table_selection not in ['1', '2', '3', 'quit']:
            print('Please choose one of the available options 1, 2, 3 or type \'quit\' to exit')
            return
        elif table_selection == 'quit':
            self.exit_search_app()
        else:
            search_key_input =  input('Enter search key: ')

        if search_key_input in searchable_fields[table_mapping[table_selection]].mandatory_fields:
            search_value = input('Enter search value: ')
            return {
                'model': self.data_sources[table_mapping[table_selection]]['model'],
                'search_key': search_key_input,
                'search_value': search_value
            }
        else:
            print(f'Sorry {search_key_input} is not a valid search key')
            print('The available search fields for your selection are as follows:')
            for field in searchable_fields[table_mapping[table_selection]].mandatory_fields:
                print(field)


