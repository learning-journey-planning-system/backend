from typing import TYPE_CHECKING
from xmlrpc.client import Boolean

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

# if TYPE_CHECKING:
#     from .role import Role

class Jobrole(Base):
    id = Column(Integer, primary_key=True) # Populates Jobrole ID
    jobrole_name = Column(String(20), nullable=False)
    deleted = Column(Boolean,default=False)
