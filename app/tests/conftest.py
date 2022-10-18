import pytest
import sqlalchemy as sa
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker

from app.db.base_class import Base
from app.main import app
from app.api.deps import get_db

from app.tests.db.init_testdb import seed_all_test_data

SQLALCHEMY_DATABASE_URL = "sqlite:///app/tests/test.db"

engine = sa.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autoflush=False, bind=engine)

# Set up the database once
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# Seed the database with test data (for primary tables)
seed_all_test_data(TestingSessionLocal())

# Seed the database with test data (for many-to-many secondary tables)
with engine.connect() as con:
    with open("app/tests/db/test_data/secondary.sql") as file:
        query = str(file.read())
        if query == "":
            print("⛔️ No secondary data to create.")
        else:
            # try:
            for line in query.split(";"):
                con.execute(line)
            print("✅ Secondary data created.")
            

# These two event listeners are only needed for sqlite for proper
# SAVEPOINT / nested transaction support. Other databases like postgres
# don't need them. 
# From: https://docs.sqlalchemy.org/en/14/dialects/sqlite.html#serializable-isolation-savepoints-transactional-ddl
@sa.event.listens_for(engine, "connect")
def do_connect(dbapi_connection, connection_record):
    # disable pysqlite's emitting of the BEGIN statement entirely.
    # also stops it from emitting COMMIT before any DDL.
    dbapi_connection.isolation_level = None


@sa.event.listens_for(engine, "begin")
def do_begin(conn):
    # emit our own BEGIN
    conn.exec_driver_sql("BEGIN")


# This fixture is the main difference to before. It creates a nested
# transaction, recreates it when the application code calls session.commit
# and rolls it back at the end.
# Based on: https://docs.sqlalchemy.org/en/14/orm/session_transaction.html#joining-a-session-into-an-external-transaction-such-as-for-test-suites
@pytest.fixture()
def session():
    connection = engine.connect()
    connection.execute("PRAGMA foreign_keys = ON")
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    # Begin a nested transaction (using SAVEPOINT).
    nested = connection.begin_nested()

    # If the application code calls session.commit, it will end the nested
    # transaction. Need to start a new one when that happens.
    @sa.event.listens_for(session, "after_transaction_end")
    def end_savepoint(session, transaction):
        nonlocal nested
        if not nested.is_active:
            nested = connection.begin_nested()

    yield session

    # Rollback the overall transaction, restoring the state before the test ran.
    session.close()
    transaction.rollback()
    connection.close()


# A fixture for the fastapi test client which depends on the
# previous session fixture. Instead of creating a new session in the
# dependency override as before, it uses the one provided by the
# session fixture.
@pytest.fixture()
def client(session):
    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    del app.dependency_overrides[get_db]