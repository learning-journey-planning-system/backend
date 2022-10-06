from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Skill(Base):
    id = Column(String(20), primary_key=True) 
    skill_name = Column(String(50), nullable=False)
    deleted = Column(Boolean, nullable=False)

    # one skill can have many courses
    courses = relationship("Course", back_populates="skills", secondary="Course_Skill")

    # one skill can have many jobroles
    jobroles = relationship("JobRole", back_populates="skills", secondary="JobRole_Skill")