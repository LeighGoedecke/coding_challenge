#!/usr/bin/python3

class Users:
    def __init__(self):
        self.name = 'Users'
        self.mandatory_fields = ['_id', 'url', 'external_id', 'name', 'alias', 'created_at', 'active', 'verified', 'shared', 'locale', 'timezone', 'last_login_at', 'email', 'phone', 'signature', 'organization_id', 'tags', 'suspended', 'role']
        self.shared_fields = {
            'organization_id': 'Organizations'
        }