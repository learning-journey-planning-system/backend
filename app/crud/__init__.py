from .crud_role import role
from .crud_staff import staff
from .crud_jobrole import jobrole
from .crud_courseskill import courseskill
from crud_jobroleskill import jobroleskill

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
