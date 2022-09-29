# backend


Naming convention: snake_case

Setup: 
1. Clone this repo
2. create testdb in mysql (make sure mamp/wamp is on)
3. edit connection string in app/core/config.py at SQLALCHEMY_DATABASE_URI

Use pipenv to run the app in virtual env -> its a better way to manage python applications and its requirements
```sh
pip install pipenv # install pipenv
pipenv shell # start a virtual env in the current dir
pipenv install --dev # install all the specified dependencies
```

Whenever you make changes to the models, restart the db:
```sh
export PYTHONPATH=$PWD
python3 app/initial_data.py # initialise db first/ refresh it
```

Run the app (make sure you are in the `backend/` dir)
```sh
uvicorn app.main:app --reload
```

<!-- shortcut to start the app:
```sh
./bootstrap.sh
``` -->

Reference: https://github.com/tiangolo/full-stack-fastapi-postgresql  
Used his implementation but simplified the app by docker, auth, celery and other unrequired utils.

Folder structure explanation:

```sh
.
├── app                    # Test files (alternatively `spec` or `tests`)
│   ├── api          # Load and stress tests
│   ├── core         # End-to-end, integration tests (alternatively `e2e`)
│   ├── core                 # Unit tests
│   ├── core 
│   ├── core 
│   ├── core 
│   ├── core 
│   ├── core 
│   └── crud
└── .gitignore
└── Pipfile
└── Pipfile.lock
└── README.md
```

│   └── crud