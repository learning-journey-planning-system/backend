from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .staff import Staff
    from .course import Course
    


class Registration(Base):
    id = Column(Integer, primary_key=True)
    course_id = Column(String(20), ForeignKey("course.id"), nullable=False)
    staff_id = Column(Integer,  ForeignKey("staff.id"), nullable=False)
    reg_status = Column(String(20), nullable=False)
    completion_status = Column(String(20), nullable=False)

    # one registration is related to one staff
    staff = relationship("Staff", back_populates="registrations")

    # one registration is related to one course
    course = relationship("Course", back_populates="registrations")
