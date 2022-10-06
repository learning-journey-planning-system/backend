from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class LearningJourney(Base):
    id = Column(Integer, primary_key=True)

    # one learningjourney is related to one staff
    staff_id = Column(Integer, ForeignKey("staff.id"), nullable=False)
    staff = relationship("Staff", back_populates="learningjourneys")

    # one learningjourney is related to one jobrole
    jobrole_id = Column(Integer, ForeignKey("jobrole.id"), nullable=False)
    jobrole = relationship("JobRole", back_populates="learningjourneys")

    # one learning journey can have many courses
    courses = relationship("Course", back_populates="learningjourneys", secondary="Course_LearningJourney")
