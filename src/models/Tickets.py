#!/usr/bin/python3

class Tickets:
    def __init__(self):
        self.name = 'Tickets'
        self.possible_fields = ['_id', 'url', 'external_id', 'created_at', 'type', 'subject', 'description', 'priority', 'status', 'submitter_id', 'assignee_id', 'organization_id', 'tags', 'has_incidents', 'due_at', 'via']
        self.associated_fields = {
            'Users': {
                '_id': ['submitter_id', 'assignee_id']
            },
            'Organizations': {
                '_id': ['organization_id']
            }
        }
