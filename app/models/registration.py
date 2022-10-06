from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Registration(Base):
    id = Column(Integer, primary_key=True)
    reg_status = Column(String(20), nullable=False)
    completion_status = Column(String(20), nullable=False)

    # one registration is related to one staff
    staff_id = Column(Integer,  ForeignKey("staff.id"), nullable=False)
    staff = relationship("Staff", back_populates="registrations")

    # one registration is related to one course
    course_id = Column(String(20), ForeignKey("course.id"), nullable=False)
    course = relationship("Course", back_populates="registrations")
