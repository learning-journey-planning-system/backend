from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base_class import Base

class Course_Skill(Base):
    skill_id = Column(String(20),ForeignKey("skill.id"), primary_key=True)
    course_id = Column(String(20), ForeignKey("course.id"), primary_key=True)

class JobRole_Skill(Base):
    jobrole_id = Column(Integer,ForeignKey("jobrole.id"), primary_key=True)
    skill_id = Column(String(20), ForeignKey("skill.id"), primary_key=True)

class Course_LearningJourney(Base):
    learningjourney_id = Column(Integer, ForeignKey("learningjourney.id"), primary_key=True)
    course_id = Column(String(20), ForeignKey("course.id"), primary_key=True)