# Enable debug mode.
DEBUG = True

# Connect to the database
SQLALCHEMY_DATABASE_URI = "<'mysql+mysqlconnector://root:root@localhost:8889/is212_example'"

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False

# copied this from the flask template given by prof
SQLALCHEMY_ENGINE_OPTIONS={'pool_size': 100,
                            'pool_recycle': 280}

