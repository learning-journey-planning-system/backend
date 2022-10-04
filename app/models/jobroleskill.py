from typing import TYPE_CHECKING
from xmlrpc.client import Boolean

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .skill import Skill
    from .jobrole import JobRole

class JobRoleSkill(Base):
    jobrole_id = Column(Integer,ForeignKey("jobrole.id"), primary_key=True) # Populates jobrole ID
    skill_id = Column(String(20), ForeignKey("skill.id"), primary_key=True) # Populates skill ID

    jobrole = relationship("JobRole", back_populates="jobroleskills")
    skill = relationship("Skill", back_populates="jobroleskills")
