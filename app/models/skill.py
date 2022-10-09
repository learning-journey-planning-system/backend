from email.policy import default
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Skill(Base):
    id = Column(Integer, primary_key=True) 
    skill_name = Column(String(50), nullable=False)
    deleted = Column(Boolean, nullable=False, default=False)

    # one skill can have many courses
    courses = relationship("Course", back_populates="skills", secondary="course_skill")

    # one skill can have many jobroles
    jobroles = relationship("JobRole", back_populates="skills", secondary="jobrole_skill")