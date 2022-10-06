from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Course(Base):
    id = Column(String(20), primary_key=True)
    course_name = Column(String(50), nullable=False)
    course_desc = Column(String(255))
    course_status = Column(String(15)) # Active or Retired
    course_type = Column(String(10)) # Internal or External 
    course_category = Column(String(50)) 

    # one course can have many skills
    skills = relationship("Skill", back_populates="courses", secondary="course_skill")

    # one course can be related to many learning journeys
    learningjourneys = relationship("LearningJourney", back_populates="courses", secondary="course_learningjourney")

    # one course can be related to many registrations
    registrations = relationship("Registration", back_populates="course")

