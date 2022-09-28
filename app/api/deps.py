from typing import Generator

from app.db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal() # creates database session
        yield db
    finally:
        db.close() # this is always executed