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
        result = {
            'message': 'No entries found.'
        }
    else:
        result = all_entries

    # Serve response as json, along with status code
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
    tags = tags.split(' ')

    if title and body:
        entry = DIARY.add_entry(title, body, tags)

        # Handle entry not created
        if not entry:
            response = jsonify({'Not created' : 'Similar entry exists'})
            response.status_code = 400
        else:
            response = jsonify({
                'entry added' : {
                    'title' : title,
                    'body' : body,
                    'tags' : tags
                }
            })
            response.status_code = 201

    else:
        response = jsonify({'Not created' : 'Title or body missing'})
        response.status_code = 400

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
            message="Error. Entry with id '{}' not found".format(id)), 404

    # Render entry as dict, if one is found
    else:
        result = {
            'entry_id': entry.entry_id,
            'entry_title': entry.entry_title,
            'entry_body': entry.entry_body,
            'entry_created_on': entry.entry_created_on,
            'entry_tags': entry.entry_tags
        }
        response = jsonify(result)
        response.status_code = 200
    return response



if __name__ == '__main__':
    api.run()
