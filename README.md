# MyDiary

## An Intro

--------

This builds out the UI templates and API backend for an online journal where users can chronicle their thoughts, feelings and dark secrets.

### UI Features

--------

The UI provides intuitive pages, with elements for user registration and login.
On login, a user can navigate to an entries page, profile page, and a settings page.
Preview available at [dmithamo/mydiary](https://dmithamo.github.io/mydiary/index.html).

**PS** : Work in Progress. Some UI elements may be unfucntional.

### API Features

--------

The API contains the endpoints below:
  
| Endpoint          | What if Does          |
| :---------------: | :-------------------: |
| GET  /entries     | Fetch all entries     |
| GET  /entries/id  | Fetch single entry    |
| POST /entries     | Add an entry          |
| POST /entries     | Add an entry          |

### Manual testing of the API

--------

To manually test the endpoints, configure and run the server as below:

1. `cd API/`

2. Run `pip install -r requirements.txt` to install dependencies

3. Run `export FLASK_APP=api/__init__.py`

4. Run `flask run` to start the server

The API is now available at `localhost:5000/mydiary/api/v1/`.
