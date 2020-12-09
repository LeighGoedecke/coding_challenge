#!/usr/bin/python3

import UserInterface


def main():
    ui = UserInterface()
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


main()
