from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .staff import Staff


class Role(Base):
    id = Column(Integer, primary_key=True)
    role_name = Column(String(20), nullable=False)

    staffs = relationship("Staff", back_populates="role")
