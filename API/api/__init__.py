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
        response = jsonify(message="No entries exist"), 404
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
            message="Not found error. Entry with id '{}' not found".format(id))
        response.status_code = 404

    # Render entry as dict, if one is found
    else:
        response = jsonify({
            'entry_id' : entry.entry_id,
            'entry_title': entry.entry_title,
            'entry_body': entry.entry_body,
            'entry_created_on': entry.entry_created_on,
            'entry_tags': entry.entry_tags
        })
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
        new_entry_params = {
            'title' : title,
            'body' : body,
            'tags' : tags
        }
        entry = DIARY.add_entry(new_entry_params)

        # Handle entry not created
        if not entry:
            response = jsonify(message='Bad request. Similar entry exists')
            response.status_code = 400
        else:
            response = jsonify({
                'entry_id' : entry.entry_id,
                'entry_title':entry.entry_title,
                'entry_body': entry.entry_body,
                'entry_created_on' : entry.entry_created_on,
                'entry_tags': entry.entry_tags
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
        response = jsonify(message="Not found error. Entry with id '{}' not found".format(id))
        response.status_code = 404

    # If entry with given id is found ...
    else:
        # Boolean flags to see if change was made after entry is found
        change_in_title = False
        change_in_body = False
        change_in_tags = False

        title = request.args.get('title')
        body = request.args.get('body')
        tags = request.args.get('tags')

        if tags:
            tags = tags.split(' ')
        else:
            tags = []
        # List of all params to update
        params_to_edit = {}

        # Check if title can be updated
        if title and title != entry.entry_title:
            params_to_edit['entry_title'] = title
            change_in_title = True

        # Check if body can be updated
        if body and entry.entry_body != body:
            params_to_edit['entry_body'] = body
            change_in_body = True

        # Check if tags can be updated
        if tags and entry.entry_tags != tags:
            params_to_edit['entry_tags'] = tags
            change_in_tags = True
        
        # Call edit_method if changes are detected
        # Send succesful PUT request response
        if change_in_title or change_in_body or change_in_tags:
            DIARY.edit_entry(entry, params_to_edit)
            response = jsonify({
                'entry_id' : entry.entry_id,
                'entry_title': entry.entry_title,
                'entry_body': entry.entry_body,
                'entry_created_on' : entry.entry_created_on,
                'entry_tags': entry.entry_tags
                }
                )
            response.status_code = 201

            # If no change made because of invalid data
        else:
            response = jsonify(message='Bad request. No changes detected')
            response.status_code = 400

    return response

@api.route('{}/entries/<int:id>'.format(BASE_URL), methods=['DELETE'])
def delete_an_entry(id):
    """
        Responds to a DELETE request to '/mydiary/api/v1/entries/id'
        endpoint
    """
    entry = DIARY.get_entry(id)
    # Handle entry not found in 'db'
    if not entry:
        response = jsonify(message="Not found error. Entry with id '{}' not found".format(id))
        response.status_code = 404

    # If entry with given id is found ...
    else:
        DIARY.delete_entry(entry)
        response = jsonify(message="Delete successful")
        response.status_code = 200

    return response


if __name__ == '__main__':
    api.run()
