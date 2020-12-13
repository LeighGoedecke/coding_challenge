#!/usr/bin/python3

class Users:
    def __init__(self):
        self.name = 'Users'
        self.possible_fields = ['_id', 'url', 'external_id', 'name', 'alias', 'created_at', 'active', 'verified', 'shared', 'locale', 'timezone', 'last_login_at', 'email', 'phone', 'signature', 'organization_id', 'tags', 'suspended', 'role']
        self.shared_fields = {
            'Organizations': {
                '_id': ['organization_id']
            },
            'Tickets': {
                'submitter_id': ['_id'],
                'assignee_id': ['_id'],
            }
        }