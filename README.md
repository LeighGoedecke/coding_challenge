# Zendesk Search

Zendesk Search is a command line application written in python which searches through company data and displays the results in a human readable format.

## About

Zendesk Search accepts json data stored within the /resources/ folder. Zendesk Search indexes the data both by primary id and by each searchable field so that searches execute quickly even as the size of the data sets increase. Based on the relationships between each data set, as defined in /src/models/, search results which directly relate to the search query are presented along with associated data.

## Getting Started
### Prerequisites
* Python 3.8
### Running
To start Zendesk Search run the following from the project's root directory:\
`./scripts/run_zendesk_search.sh`
### Tests
To run tests run the following from the project's root directory:\
`./scripts/run_tests.sh`

## Design Decisions, Assumptions and Tradeoffs

Zendesk Search separately organises user, organization and ticket data into an inverted index. This means that the each lookup occurs in constant time regardless of the size of the data set. However indexing the data in this way uses a relatively larger amount of memory than if we were to simply loop through each data set to perform the search.

The search app assumes that each `_id` value is unique within it's category (users, organizations, tickets) and must be present for each data element. It is also assumed that the mandatory fields as defined in /src/models/ are an exhaustive set of the possible fields for each category - no fields other than what's specified within `possible_fields` can be provided.

## Screenshots