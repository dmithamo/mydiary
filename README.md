# MyDiary

This repo is a build out of the UI templates and API backend for an online journal where users can chronicle their thoughts, feelings and dark secrets.

## UI Features

The UI provides intuitive pages, with elements for user registration and login.
On login, a user can navigate to an entries page, profile page, and a settings page.
Preview available at [dmithamo/mydiary](https://dmithamo.github.io/mydiary/index.html).

**PS** : Work in Progress. Some UI elements may be unfucntional.

## API Features

The API contains the endpoints below:
  
| Endpoint               | What if Does             | Git Branch                          |
| :--------------------  | :----------------------- | :--------------------------------   |
| GET  /entries          | Fetch all entries        | ft-api-fetch-all-entries-159100964  |
| GET  /entries/id       | Fetch single entry       | ft-api-fetch-single-entry-159101143 |
| POST /entries          | Add an entry             | ft-api-add-entry-159101428          |
| PUT /entries/id        | Modify an entry          | ft-api-modify-entry-159101719       |
| DELETE /entries/id     | Delete an entry          | ft-api-delete-entry-159102048       |

## Manual testing of the API

To manually test the endpoints, configure and run the server as below:

1. `git checkout <relevant-branch>` or `git checkout <develop-branch>` for all the endpoints

2. `cd API/`

3. Run `pip install -r requirements.txt` to install dependencies

4. Run `export FLASK_APP=api/__init__.py`

5. Run `flask run` to start the server

The API is now available at `localhost:5000/mydiary/api/v1/`.
