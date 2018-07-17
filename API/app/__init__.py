"""
    Module initializes a Flask instance and defines the app's
    routes.
"""

from flask import Flask, jsonify
from models import Entry


# Constant BASE_URL is prefixed to each route
BASE_URL = '/mydiary/api/v1'

app = Flask(__name__)


@app.route('{}/entries'.format(BASE_URL), methods=['GET'])
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
    if len(all_entries) == 0:
        result = {
            'message' : 'No entries yet.'
        }
    else:
        result = all_entries

    # Serve response as json, along with status code
    response = jsonify(result)
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run()
