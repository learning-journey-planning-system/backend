from email.policy import default
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .courseskill import Courseskill

class Course(Base):
    id = Column(String(20), primary_key=True)
    course_name = Column(String(50))
    course_desc = Column(String(255))
    course_status = Column(String(15)) # Active or Retired
    course_type = Column(String(10)) # Internal or External 
    course_category = Column(String(50)) 
    deleted = Column(Boolean)

    courseskill = relationship("Courseskill", back_populates="course")

