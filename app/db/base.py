# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.role import Role  # noqa
from app.models.staff import Staff  # noqa
from app.models.jobrole import Jobrole  # noqa
from app.models.jobroleskill import Jobroleskill  # noqa
from app.models.courseskill import Courseskill  # noqa

