# backend


Naming convention: snake_case

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
