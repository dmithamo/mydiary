"""
    Module initializes a Flask instance and defines the app's
    routes.
"""

from flask import Flask, jsonify, abort
from app.models import Entry
import config

# Constant BASE_URL is prefixed to each route
BASE_URL = '/mydiary/api/v1'

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)


@app.route('{}/entries/'.format(BASE_URL), methods=['GET'])
def fetch_all_entries():
    """
        Responds to a GET request to '/mydiary/api/v1/entries'
        endpoint
    """
    all_entries = []

    # Loop through list of entries from Entries.entries
    # Render each as a dict with properties as key-value pairs
    for entry in Entry.get_all_entries():
        entry_as_dict = {
            'entry_id': entry.entry_id,
            'entry_title': entry.entry_title,
            'entry_body': entry.entry_body,
            'entry_timestamp': entry.entry_timestamp,
            'entry_tags': entry.entry_tags
        }
        # Add dict version of entry to all_entries list
        all_entries.append(entry_as_dict)

    # Handle empty all_entries list
    if not all_entries:
        result = {
            'message': 'No entries yet.'
        }
    else:
        result = all_entries

    # Serve response as json, along with status code
    response = jsonify(result)
    response.status_code = 200
    return response

@app.route('{}/entries/<int:entry_id>/'.format(BASE_URL), methods=['GET'])
def fetch_single_entry(entry_id):
    """
    Responds to a GET request to '/mydiary/api/v1/entries/id'
    endpoint
    """
    entry = Entry.get_single_entry(entry_id)

    # Handle no id found (result=None)
    if not entry:
        response = jsonify(message="Error. Entry with id '{}' not found".format(entry_id)), 404

    # Render entry as dict, if one is found
    else:
        result = {
            'entry_id': entry.entry_id,
            'entry_title': entry.entry_title,
            'entry_body': entry.entry_body,
            'entry_timestamp': entry.entry_timestamp,
            'entry_tags': entry.entry_tags
        }
        response = jsonify(result)
        response.status_code = 200
    return response


if __name__ == '__main__':
    app.run()
