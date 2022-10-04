from .base import CRUDBase
from app.models.courseskill import Courseskill
from app.schemas.courseskill import CourseskillCreate, CourseskillUpdate

courseskill = CRUDBase[Courseskill, CourseskillCreate, CourseskillUpdate](Courseskill)
