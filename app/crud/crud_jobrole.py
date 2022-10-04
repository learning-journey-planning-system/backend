from .base import CRUDBase
from app.models.jobrole import Jobrole
from app.schemas.jobrole import JobroleCreate, JobroleUpdate

jobrole = CRUDBase[Jobrole, JobroleCreate, JobroleUpdate](Jobrole)