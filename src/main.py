#!/usr/bin/python3

from UserInterface import UserInterface
from DataStore import DataStore
from SearchEngine import SearchEngine
from models.Users import Users
from models.Tickets import Tickets
from models.Organizations import Organizations
from data_reader import read_data


def main():
    data_sources = {
        "Users": {
            "source": "resources/users.json",
            "model": Users()
        },
        "Organizations": {
            "source": "resources/organizations.json",
            "model": Organizations()
        },
        "Tickets": {
            "source": "resources/tickets.json",
            "model": Tickets()
        }
    }

    ui = UserInterface(data_sources)

    try:
        index = {}
        for record_type in data_sources:
            source_file = data_sources[record_type]["source"]
            model = data_sources[record_type]["model"]
            data = read_data(source_file)
            index[record_type] = DataStore(model, data).index_data()
    except (ValueError, KeyError) as e:
        print(e)
        return

    ui.display_intro()
    while True:
        search_selection = ui.retrieve_search_option()
        if search_selection == '1':
            # TODO make broken search params not break search logic
            search_params = ui.retrieve_search_params()
            if search_params:
                search_engine = SearchEngine(index, search_params)
                search_results = search_engine.search()
                ui.display_search_data(search_results)
        elif search_selection == '2':
            ui.display_all_searchable_fields(ui.retrieve_searchable_fields())
        elif search_selection == 'quit':
            ui.exit_search_app()
        else:
            ui.display_search_options()


if __name__ == "__main__":
    main()