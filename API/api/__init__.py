"""
    Module initializes a Flask instance and defines the api's
    routes.
"""

from flask import Flask, request, jsonify, json, abort
from api.models import Diary, Entry
import config

# Constant BASE_URL is prefixed to each route
BASE_URL = '/mydiary/api/v1'

api = Flask(__name__)
api.config.from_object(config.DevelopmentConfig)

# Create an instance of the Diary class - represents db
DIARY = Diary()


@api.route('{}/entries'.format(BASE_URL), methods=['GET'])
@api.route('{}/entries/'.format(BASE_URL), methods=['GET'])
def fetch_all_entries():
    """
        Responds to a GET request to '/mydiary/api/v1/entries'
        endpoint
    """
    all_entries = []

    # Loop through list of entry objects from Diary.entries
    # Render each as a dict with properties as key-value pairs
    for entry in DIARY.get_entries():
        entry_as_dict = {
            'entry_id': entry.entry_id,
            'entry_title': entry.entry_title,
            'entry_body': entry.entry_body,
            'entry_created_on': entry.entry_created_on,
            'entry_tags': entry.entry_tags
        }
        # Add dict version of entry to all_entries list
        all_entries.append(entry_as_dict)

    # Handle empty all_entries list
    if not all_entries:
        response = jsonify(message="No entries exist"), 400
    else:
        result = all_entries
        # Serve response as json, along with status code
        response = jsonify(result)
        response.status_code = 200
    return response


@api.route('{}/entries/<int:id>'.format(BASE_URL), methods=['GET'])
def fetch_single_entry(id):
    """
        Responds to a GET request to '/mydiary/api/v1/entries/id'
        endpoint
    """
    entry = DIARY.get_entry(id)

    # Handle no id found (result=None)
    if not entry:
        response = jsonify(
            message="Not found error. Entry with id '{}' not found".format(id)), 404

    # Render entry as dict, if one is found
    else:
        result = {
            'entry_title': entry.entry_title,
            'entry_body': entry.entry_body,
            'entry_created_on': entry.entry_created_on,
            'entry_tags': entry.entry_tags
        }
        response = jsonify(result)
        response.status_code = 200
    return response


@api.route('{}/entries'.format(BASE_URL), methods=['POST'])
def add_an_entry():
    """
        Responds to a POST request to '/mydiary/api/v1/entries'
        endpoint
    """
    title = request.args.get('title')
    body = request.args.get('body')
    tags = request.args.get('tags')
    if tags:
        tags = tags.split(' ')
    else:
        tags = []

    if title and body:
        entry = DIARY.add_entry(title, body, tags)

        # Handle entry not created
        if not entry:
            response = jsonify(message='Bad request. Similar entry exists'), 400
        else:
            response = jsonify({
                'title': title,
                'body': body,
                'entry_created_on' : entry.entry_created_on,
                'tags': tags
                }
                )
            response.status_code = 201

    else:
        response = jsonify(message='Bad request. Title or body missing')
        response.status_code = 400

    return response

@api.route('{}/entries/<int:id>'.format(BASE_URL), methods=['PUT'])
def modify_an_entry(id):
    """
        Responds to a PUT request to '/mydiary/api/v1/entries/id'
        endpoint
    """

    entry = DIARY.get_entry(id)
    # Handle entry not found in 'db'
    if not entry:
        response = jsonify(message="Not found error. Entry with id '{}' not found".format(id)), 404
    # If entry with given id is found ...
    else:
        title = request.args.get('title')
        body = request.args.get('body')
        tags = request.args.get('tags')

        if tags:
            tags = tags.split(' ')
        else:
            tags = []
        # If request contains ANY of these params
        if title or body or tags:
            # Collect entry_properties to change in dict
            properties_to_edit = {
                'entry_title' : title,
                'entry_body' : body,
                'entry_tags' : tags
            }

            # If any of these params is different from the entry's params ...
            #  proced to edit, send 'successful PUT' response
            if entry.entry_title != title or entry.entry_body != body \
            or entry.entry_tags != tags:

                DIARY.edit_entry(entry, properties_to_edit)

                response = jsonify({
                    'title': title,
                    'body': body,
                    'entry_created_on' : entry.entry_created_on,
                    'tags': tags
                    }
                    )
                response.status_code = 201
            # Handle no changes detected
            else:
                response = jsonify(message="Bad request. No changes detected"), 400
        # Handle params to edit not provided
        else:
            response = jsonify(message='Bad request. No data provided'), 400
            response.status_code = 400

    return response


if __name__ == '__main__':
    api.run()
