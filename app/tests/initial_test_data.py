import logging

from app.tests.db.session import TestingSessionLocal
from app.tests.db.init_testdb import init_testdb

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_test_data() -> None:
    db = TestingSessionLocal()
    init_testdb(db)

def main() -> None:
    logger.info("Creating initial test data")
    init_test_data()
    logger.info("Initial test data created")


if __name__ == "__main__":
    main()