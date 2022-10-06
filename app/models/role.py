from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Role(Base):
    id = Column(Integer, primary_key=True)
    role_name = Column(String(20), nullable=False)

    # one role can have many staffs
    staffs = relationship("Staff", back_populates="role")
