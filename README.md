# Zendesk Search :telescope:

Zendesk Search is a command line application written in python which searches through company data and displays the results in a human readable format.

## About

Zendesk Search accepts json data stored within the `/resources/` folder. Users input which data set they'd like to search against and Zendesk Search presents data directly related to the search query along with associated data. Relationships between data sets are specified within `/src/models/`.

## Getting Started
### Prerequisites
* Python 3.8
### Running
To start Zendesk Search run the following from the project's root directory:\
`./scripts/run_zendesk_search.sh`
### Tests
To run tests run the following from the project's root directory:\
`./scripts/run_tests.sh`

## Design Decisions and Tradeoffs

I chose to organise user, organization and ticket data into two data sets each - the first set is indexed by the primary id `_id` and the second set is indexed by each of the searchable fields. There is a memory cost associated with indexing the data like this since all records are essentially stored twice, however an inverted index allows lookups to occur in constant time regardless of the size of the data set. 

## Assumptions

* Each `_id` value is unique within its category (users, organizations, tickets) and must be present for each data element. 
* Mandatory fields as defined in `/src/models/` are an exhaustive set of the possible fields for each category - no fields other than what's specified within `possible_fields` can be provided.
* Only the numeric id fields are shared between data sets. This application does not look for shared tags between users/tickets/organizations.


## Screenshots

