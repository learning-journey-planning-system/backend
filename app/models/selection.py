from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .learningjourney import LearningJourney
    from .course import Course


class Selection(Base):
    learningjourney_id = Column(Integer, ForeignKey("learningjourney.id"), primary_key=True)
    course_id = Column(String(20), ForeignKey("course.id"), primary_key=True)

    # one selection is related to one learningjourney
    learningjourney = relationship("LearningJourney", back_populates="selections")

    # one selection is related to one course
    course = relationship("Course", back_populates="selections")
