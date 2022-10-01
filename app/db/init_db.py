from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import text
from app.db.base_class import Base
from app.db.session import engine
import app.db.base
# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line

    # Create database if it does not exist.
    if not database_exists(engine.url):
        create_database(engine.url)

    # else, drop all tables
    elif database_exists(engine.url):
        Base.metadata.drop_all(bind=engine)
    
    # Create tables.
    Base.metadata.create_all(bind=engine)

    # Seed initial data.
    with engine.connect() as con:
        with open("./G10T3LJPSDB.sql") as file:
            query = str(file.read())
            for line in query.split(";"):
                con.execute(line)