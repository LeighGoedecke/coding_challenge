#!/usr/bin/python3

class Organizations:
    def __init__(self):
        self.name = 'Organizations'
        self.mandatory_fields = ['_id', 'url', 'external_id', 'name', 'domain_names', 'created_at', 'details', 'shared_tickets', 'tags']
        self.shared_fields = {
            'Tickets': {
                'organization_id': ['_id']
            },
            'Users': {
                'organization_id': ['_id']
            }
        }
