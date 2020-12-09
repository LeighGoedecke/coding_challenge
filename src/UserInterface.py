#!/usr/bin/python3

class UserInterface:
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
        # TODO fix this so it's not terrible
        searchable_fields = {}
        for filename in ['organizations.json', 'tickets.json', 'users.json']:
            with open(f'resources/{filename}') as f:
                info_category = filename[:-5].capitalize()
                searchable_fields[info_category] = list(json.loads(f.read())[0].keys())
        return searchable_fields

    def display_searchable_fields(self, searchable_fields):
        for category in searchable_fields:
            print('----------------------------------')
            print(f'Search {category} with:')
            for field in searchable_fields[category]:
                print(field)

    def orchestrate_search(self):
        searchable_fields = self.retrieve_searchable_fields()
        table_mapping = {
            '1': 'Users',
            '2': 'Tickets',
            '3': 'Organizations'
        }

        search_selection = input('Select 1) Users, 2) Tickets, or 3) Organizations\n')
        if search_selection not in ['1', '2', '3', 'quit']:
            print('Please choose one of the available options 1, 2, 3 or type \'quit\' to exit')
        elif search_selection == 'quit':
            self.exit_search_app()
        else:
            search_key = input('Enter search key: ')

        if search_key in searchable_fields[table_mapping[search_selection]]:
            search_value = input('Enter search value: ')
            # search_engine(search_selection, search_value)
        else:
            print(f'Sorry {search_key} is not a valid search key')
            print('The available search fields for your selection are as follows:')
            for field in searchable_fields[table_mapping[search_selection]]:
                print(field)
