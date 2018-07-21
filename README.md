# MyDiary

This repo is a build out of the UI templates and API backend for an online journal.

## UI Features

The UI provides elements for :

1. User registration and login.

2. Once logged in, pages where entries, user profile and user settings can be viewed an modified.

UI preview : [dmithamo/mydiary](https://dmithamo.github.io/mydiary/index.html).

Code for UI tracked in the [gh-pages](https://github.com/dmithamo/mydiary/tree/gh-pages) branch.

## API Features

The API contains the endpoints below:
  
| Endpoint               | What if Does             | Git Branch                          |
| :--------------------  | :----------------------- | :--------------------------------   |
| GET  /entries          | Fetch all entries        | [ft-api-fetch-all-entries-159100964](https://github.com/dmithamo/mydiary/tree/ft-api-fetch-all-entries-159100964)  |
| GET  /entries/id       | Fetch single entry       | [ft-api-fetch-single-entry-159101143](https://github.com/dmithamo/mydiary/tree/ft-api-fetch-single-entry-159101143) |
| POST /entries          | Add an entry             | [ft-api-add-entry-159101428](https://github.com/dmithamo/mydiary/tree/ft-api-add-entry-159101428)          |
| PUT /entries/id        | Modify an entry          | [ft-api-modify-entry-159101719](https://github.com/dmithamo/mydiary/tree/ft-api-modify-entry-159101719)       |
| DELETE /entries/id     | Delete an entry          | [ft-api-delete-entry-159102048](https://github.com/dmithamo/mydiary/tree/ft-api-delete-entry-159102048)       |

## Manual testing of the API

To manually test the endpoints, configure and run the server as below:

1. `git checkout <relevant-branch>` or `git checkout <develop-branch>` for all the endpoints

2. `cd API/`

3. Create and activate a [Virtual Environment](https://virtualenv.pypa.io/en/stable/).

4. Run `pip install -r requirements.txt` to install dependencies

5. Run `export FLASK_APP=api/__init__.py`

6. Run `flask run` to start the server

Test the API's endpoints at `localhost:5000/mydiary/api/v1/`.

Recommended testing tool : [Postman](https://www.getpostman.com/).

## Pytest-ing the API

To run the tests written for the API's endpoints:

1. Proceed as in steps `1 to 4` above.

2. Run `pytest` (or `pytest -v` for verbose output)

[Pytest documentation](http://pytest-flask.readthedocs.io/en/latest/).
