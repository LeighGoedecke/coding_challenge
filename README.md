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
Search UI\
<img width="516" alt="Screen Shot 2020-12-14 at 1 13 15 am" src="https://user-images.githubusercontent.com/29794761/102014347-8c724b00-3da9-11eb-927d-c5aa880a33b8.png">

Displaying data directly associated with the search query:
<img width="595" alt="Screen Shot 2020-12-14 at 1 14 49 am" src="https://user-images.githubusercontent.com/29794761/102014389-c6435180-3da9-11eb-845a-2351cfa1c703.png">

Displaying associated organization and ticket
<img width="581" alt="Screen Shot 2020-12-14 at 1 17 08 am" src="https://user-images.githubusercontent.com/29794761/102014448-191d0900-3daa-11eb-82c9-42d70eb1d09e.png">


