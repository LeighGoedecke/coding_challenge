import unittest
from src.DataStore import DataStore
from src.models.Tickets import Tickets

some_data = [{
                "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
                "url": "http://initech.zendesk.com/api/v2/tickets/436bf9b0-1147-4c0a-8439-6f79833bff5b.json",
                "external_id": "9210cdc9-4bee-485f-a078-35396cd74063",
                "created_at": "2016-04-28T11:19:34 -10:00",
                "type": "incident",
                "subject": "A Catastrophe in Korea (North)",
                "description": "Nostrud ad sit velit cupidatat laboris ipsum nisi amet laboris ex exercitation amet et proident. Ipsum fugiat aute dolore tempor nostrud velit ipsum.",
                "priority": "high",
                "status": "pending",
                "submitter_id": 38,
                "assignee_id": 24,
                "organization_id": 116,
                "tags": [
                    "Ohio",
                    "Pennsylvania",
                    "American Samoa",
                    "Northern Mariana Islands"
                ],
                "has_incidents": False,
                "due_at": "2016-07-31T02:37:50 -10:00",
                "via": "web"
            },
{
    "_id": "1a227508-9f39-427c-8f57-1b72f3fab87c",
    "url": "http://initech.zendesk.com/api/v2/tickets/1a227508-9f39-427c-8f57-1b72f3fab87c.json",
    "external_id": "3e5ca820-cd1f-4a02-a18f-11b18e7bb49a",
    "created_at": "2016-04-14T08:32:31 -10:00",
    "type": "incident",
    "subject": "A Catastrophe in Micronesia",
    "description": "Aliquip excepteur fugiat ex minim ea aute eu labore. Sunt eiusmod esse eu non commodo est veniam consequat.",
    "priority": "low",
    "status": "hold",
    "submitter_id": 71,
    "assignee_id": 38,
    "organization_id": 112,
    "tags": [
        "Puerto Rico",
        "Idaho",
        "Oklahoma",
        "Louisiana"
    ],
    "has_incidents": False,
    "due_at": "2016-08-15T05:37:32 -10:00",
    "via": "chat"
}
]


class TestDataStore(unittest.TestCase):
    def test_index_data_has_correct_schema(self):
        data = DataStore(Tickets(), some_data)
        indexed_data = data.index_data()
        self.assertEqual(list(indexed_data.keys()), ['id_index', 'field_index'])
        # make simple model class and simple data set and assertequal an entire index

class TestSearchEngine(unittest.TestCase):
    def test_successful_search_by_id(self):
        # create an index object at start of test file
        # create a dummy class
        #assert that the test finds the falue
        pass

    def test_null_search_by_id(self):
        #same thing but search for bad value
        pass

    def test_successful_search_by_field(self)
        pass

    def test_null_search_by_field(self):
        pass

    def test_search_by_tag_field(self):
        pass


# TEST DATA READER MOCKING

# TEST PLUGGING DATASTORE INTO SEARCH ENGINE








if __name__ == '__main__':
    unittest.main()
