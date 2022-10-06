from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Staff(Base):
    id = Column(Integer, primary_key=True) # user logs in with this
    staff_fname = Column(String(50), nullable=False)
    staff_lname = Column(String(50), nullable=False)
    dept = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    # one staff has one role
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)
    role = relationship("Role", back_populates="staffs")

    # one staff can have many learningjourneys
    learningjourneys = relationship("LearningJourney", back_populates="staff")

    # one staff can make many registrations
    registrations = relationship("Registration", back_populates="staff")