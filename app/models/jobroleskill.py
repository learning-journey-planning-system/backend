from typing import TYPE_CHECKING
from xmlrpc.client import Boolean

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .skill import Skill
    from .jobrole import Jobrole

class Jobroleskill(Base):
    id = Column(Integer,ForeignKey("jobrole.id"), primary_key=True) # Populates jobrole ID
    skillid = Column(String(20), ForeignKey("skill.id"), primary_key=True) # Populates skill ID

    skill = relationship("Skill", back_populates="skills")
    jobrole = relationship("Jobrole", back_populates="jobroles")
