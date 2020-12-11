#!/usr/bin/python3

from UserInterface import UserInterface
from DataStore import DataStore
from Users import Users
from Tickets import Tickets
from Organizations import Organizations
from data_reader import data_reader


def main():
    ui = UserInterface()
    indexed_data = []
    data_sources = {
        'resources/organizations.json': Organizations(),
        'resources/tickets.json': Tickets(),
        'resources/users.json': Users()
    }

    for source in data_sources:
        data = data_reader(source)
        indexed_data.append(DataStore(data_sources[source], data))

    ui.display_intro()
    while True:
        search_selection = ui.retrieve_search_option()
        if search_selection == '1':
            ui.orchestrate_search()
        elif search_selection == '2':
            ui.display_searchable_fields(ui.retrieve_searchable_fields())
        elif search_selection == 'quit':
            ui.exit_search_app()
        else:
            print('Please choose from options \'1\', \'2\' or type \'quit\'')


if __name__ == "__main__":
    main()