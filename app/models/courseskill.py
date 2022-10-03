from typing import TYPE_CHECKING
from xmlrpc.client import Boolean

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .skill import Skill
    from .course import Course

class Courseskill(Base):
    id = Column(String(20),ForeignKey("skill.id"), primary_key=True) # Populates skill ID
    courseid = Column(String(20), ForeignKey("course.id"), primary_key=True) # Populates course ID

    skill = relationship("Skill", back_populates="courseskills")
    course = relationship("Course", back_populates="courseskill")
