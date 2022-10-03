from .base import CRUDBase
from app.models.jobroleskill import Jobroleskill
from app.schemas.jobroleskill import JobroleskillCreate, JobroleskillUpdate

jobroleskill = CRUDBase[Jobroleskill, JobroleskillCreate, JobroleskillUpdate](Jobroleskill)