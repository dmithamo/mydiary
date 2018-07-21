"""
    Lays out the functional tests for this API's endpoints.
"""


import pytest
import json

from api import api
import config

# Part of api url common to all endpoints
BASE_URL = '/mydiary/api/v1'

# Reusable entry_params
SAMPLE_ENTRY_PARAMS_1 = {
    'title' : 'Dennis the Me',
    'body' : 'My name is Dennis and I yam',
    'tags' : 'tag one too'
}

SAMPLE_ENTRY_PARAMS_2 = {
    'title' : 'Who let',
    'body' : 'Did you let them out',
    'tags' : 'the dogs'
}

# Function wide scope - runs once per test
@pytest.fixture(scope='module') 
def api_test_client():
    """
        Generate API instance that will respond to requests to the
        API. Runs before each test
    """
    api_instance = api
    api_instance.config.from_object(config.TestingConfig)
    api_test_client = api_instance.test_client()

    # Define the context within which requests to the api_test_client
    # will be made.
    api_context = api_instance.app_context()
    api_context.push()
    yield api_test_client
    # Remove context after yielding api_test_client
    api_context.pop()

def test_get_entries_1(api_test_client):
    """
        1. Test 'GET /entries' - when no entries exist
    """
    response = api_test_client.get('{}/entries'.format(BASE_URL))
    assert response.status_code == 404
    assert 'No entries exist' in str(response.data)

def test_get_entries_2(api_test_client):
    """
        2. Test 'GET /entries/id' - when entry does not exist
    """
    response = api_test_client.get('{}/entries/1'.format(BASE_URL))
    assert response.status_code == 404
    assert 'Not found error. Entry with' in str(response.data)

def test_post_entries_1(api_test_client):
    """
        3. Test 'POST /entries' - with all required params present
    """
    response = api_test_client.post('{}/entries?title={}&body={}&tags={}'.format(
        BASE_URL, SAMPLE_ENTRY_PARAMS_1['title'],
        SAMPLE_ENTRY_PARAMS_1['body'], SAMPLE_ENTRY_PARAMS_1['tags'] 
        ))
    assert response.status_code == 201
    assert 'Dennis the Me' in str(response.data)

def test_post_entries_2(api_test_client):
    """
        4. Test 'POST /entries' - with a required param missing
    """
    response = api_test_client.post('{}/entries?title={}'.format(
        BASE_URL, SAMPLE_ENTRY_PARAMS_2['title']
        ))
    assert response.status_code == 400
    assert 'Title or body missing' in str(response.data)

def test_post_entries_3(api_test_client):
    """
        5. Test 'POST /entries' - when entry with similar params exists
    """
    response = api_test_client.post('{}/entries?title={}&body={}'.format(
        BASE_URL, SAMPLE_ENTRY_PARAMS_1['title'], SAMPLE_ENTRY_PARAMS_1['body']
        ))
    assert response.status_code == 400
    assert 'Similar entry exists' in str(response.data)
