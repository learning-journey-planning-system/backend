# backend


Naming convention: snake_case

### Setup: 
1. Clone this repo
2. create testdb in mysql (make sure mamp/wamp is on)
3. edit connection string in app/core/config.py at SQLALCHEMY_DATABASE_URI

4. Use pipenv to run the app in virtual env -> its a better way to manage python applications and its requirements
```sh
pip install pipenv          # install pipenv
pipenv shell                # start a virtual env in the current dir
pipenv install --dev        # install all the specified dependencies
```

5. Whenever you make changes to the models, restart the db:
```sh
export PYTHONPATH=$PWD
python3 app/initial_data.py # initialise db first/ refresh it
```

6. Run the app (make sure you are in the `backend/` dir)
```sh
uvicorn app.main:app --reload
```

<!-- shortcut to start the app:
```sh
./bootstrap.sh
``` -->

### Reference
[full-stack-fastapi-postgresql by tiangolo](https://github.com/tiangolo/full-stack-fastapi-postgresql)  
[his documentation](https://fastapi.tiangolo.com/)  
Used his implementation but simplified the app by docker, auth, celery and other unrequired utils.

### Folder structure explanation:

##### Overview:
```sh
.
├── app                         # The entire api module
│   ├── api                     # Api endpoints
│   ├── core                    # Methods for development (eg. settings)
│   ├── crud                    # Adds CRUD methods for each model
│   ├── db                      # Methods to manage database
│   ├── models                  # Description of the objects we need, SQLAlchemy maps these models
│   ├── schemas                 # Define input/return formats for apis
│   ├── tests                   # Unit tests (ignore for now)
│   ├── __init__.py             # Present in every folder to modularize the directories
│   ├── initial_data.py         # Script to connect to and initialise database
│   └── main.py                 # Runs the API application
└── .gitignore                  # Specifies files to be ignored by .git
└── Pipfile                     # Specifies requirements and dependencies for the app
└── Pipfile.lock                # Autogenerated cache by pipenv
└── README.md
```

##### All files (not done yet)
```sh
.
├── app                         # The entire api module
│   ├── api                     # 
│   │   ├── api_v1              #
│   │   │   ├── endpoints
│   │   │   │   ├── __init__.py 
│   │   │   │   ├── roles.py
│   │   │   │   └── staffs.py
│   │   │   ├── __init__.py 
│   │   │   └── api.py
│   │   ├── __init__.py 
│   │   └── deps.py
│   ├── core                      # 
│   │   ├── __init__.py 
│   │   └── config.py
│   ├── crud                      # 
│   │   ├── __init__.py 
│   │   ├── base.py 
│   │   ├── crud_role.py 
│   │   └── crud_staff.py
│   ├── db 
│   │   ├── __init__.py 
│   │   ├── base_class.py 
│   │   ├── base.py 
│   │   ├── init_db.py 
│   │   └── session.py
│   ├── models 
│   │   ├── __init__.py 
│   │   ├── role.py 
│   │   └── staff.py
│   ├── schemas 
│   │   ├── __init__.py 
│   │   ├── msg.py 
│   │   ├── role.py 
│   │   └── staff.py
│   ├── tests 
│   ├── __init__.py 
│   ├── initial_data.py
│   └── main.py
└── .gitignore
└── Pipfile
└── Pipfile.lock
└── README.md
```
