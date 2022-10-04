from typing import TYPE_CHECKING
from xmlrpc.client import Boolean

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .jobroleskill import JobRoleSkill
    from .learningjourney import LearningJourney

class JobRole(Base):
    id = Column(Integer, primary_key=True) # Populates Jobrole ID
    jobrole_name = Column(String(20), nullable=False)
    deleted = Column(Boolean, default = False)

    jobroleskills = relationship("JobRoleSkill", back_populates="jobrole")

    learningjourneys = relationship("LearningJourney", back_populates="jobrole")

    
