from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .staff import Staff
    from .jobrole import JobRole
    from .selection import Selection


class LearningJourney(Base):
    id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey("staff.id"), nullable=False)
    jobrole_id = Column(Integer, ForeignKey("jobrole.id"), nullable=False)

    # one learningjourney is related to one staff
    staff = relationship("Staff", back_populates="learningjourneys")

    # one learningjourney is related to one jobrole
    jobrole = relationship("JobRole", back_populates="learningjourneys")

    # one learning journey can have many selections
    selections = relationship("Selection", back_populates="learningjourney")
