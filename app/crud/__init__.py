from .crud_course import course
from .crud_jobrole import jobrole
from .crud_role import role
from .crud_staff import staff
from .crud_skill import skill
from .crud_registration import registration
from .crud_learningjourney import learningjourney

from .crud_course import CRUDCourse
from .crud_jobrole import CRUDJobRole
from .crud_learningjourney import CRUDLearningJourney
from .crud_registration import CRUDRegistration
from .crud_role import CRUDRole
from .crud_skill import CRUDSkill
from .crud_staff import CRUDStaff

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
