# backend


Naming convention: snake_case

<!--### 1. Shortcut to start the app:
1. Ensure MAMP/WAMP is on
2. Ensure you have pipenv installed
3. Execute the following script in the cli:
```sh
./start_backend.sh
```-->

### 1. Setup: 
1. Clone backend repo
2. Ensure you are on backend directory and main branch 
3. Check that your python version is at least 3.9  
4. On MAMP/WAMP
5. edit connection string in `app/core/config.py` at `SQLALCHEMY_DATABASE_URI` (you can use sql alchemy to help you test your connection)

4. Use `pipenv` to run the app in virtual env -> its a better way to manage python applications and its requirements
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
7. Go to 127.0.0.1:8000/docs on your chrome browser to see the outputs of the APIs 

### 2. To stop the backend service and exit the pipenv shell
1. Stop backend service: ctrl + C
2. Exit pipenv shell: ctrl + D

### 3. Reference
[full-stack-fastapi-postgresql by tiangolo](https://github.com/tiangolo/full-stack-fastapi-postgresql)  
[his documentation](https://fastapi.tiangolo.com/)  
Used his implementation but simplified the app by docker, auth, celery and other unrequired utils.

### 4. Folder structure explanation:

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

##### All files (excludes explanation for test files)
```sh
.
├── app                         
│   ├── api                     
│   │   ├── api_v1              # apis are organised into versions (for ease of management in future releases)
│   │   │   ├── endpoints       
│   │   │   │   ├── __init__.py 
│   │   │   │   ├── roles.py    # all endpoints relating to one model is stored in one file
│   │   │   │   └── staffs.py   
│   │   │   ├── __init__.py     
│   │   │   └── api.py          # file to add endpoints to router
│   │   ├── __init__.py         
│   │   └── deps.py             # to create a database session for endpoints to retrieve data from
│   ├── core                    
│   │   ├── __init__.py         
│   │   └── config.py           # stores all settings variables
│   ├── crud                    
│   │   ├── __init__.py         
│   │   ├── base.py             # base model for all crud classes
│   │   ├── crud_role.py        # indiv crud class for each model 
│   │   └── crud_staff.py       # to add more specialised CRUD methods that are not in the base class
│   ├── db                      
│   │   ├── __init__.py         
│   │   ├── base_class.py       # base class for models
│   │   ├── base.py             # Import all the models, so that Base has them before being imported by Alembic
│   │   ├── init_db.py          # method to initialise db
│   │   └── session.py          # creates a session object
│   ├── models                  
│   │   ├── __init__.py         
│   │   ├── role.py             # each table will have its own class, one file for one table in the db
│   │   └── staff.py            
│   ├── schemas                 
│   │   ├── __init__.py         
│   │   ├── msg.py              # define format for error/success msgs
│   │   ├── role.py             # each model has its own file to define its input/return formats
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
