from .base import CRUDBase
from app.models.jobrole import JobRole
from app.schemas.jobrole import JobRoleCreate, JobRoleUpdate

jobrole = CRUDBase[JobRole, JobRoleCreate, JobRoleUpdate](JobRole)