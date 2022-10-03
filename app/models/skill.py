from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .courseskill import Courseskill
    from .jobroleskill import Jobroleskill

class Skill(Base):
    id = Column(String(20), primary_key=True) 
    skill_name = Column(String(50), nullable=False)
    deleted = Column(Boolean, nullable=False)

    courseskills = relationship("Courseskill", back_populates="skill")
    skills = relationship("Jobroleskill", back_populates="skill")