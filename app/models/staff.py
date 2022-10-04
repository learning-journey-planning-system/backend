from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.api.api_v1.endpoints import registration

from app.db.base_class import Base
from app.models import learningjourney

if TYPE_CHECKING:
    from .role import Role

class Staff(Base):
    id = Column(Integer, primary_key=True) # user logs in with this
    staff_fname = Column(String(50), nullable=False)
    staff_lname = Column(String(50), nullable=False)
    dept = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)

    role = relationship("Role", back_populates="staffs")

    learningjourneys = relationship("LearningJourney", back_populates="staff")
    registrations = relationship("Registration", back_populates="staff")