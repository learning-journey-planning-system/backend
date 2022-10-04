from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Skill(Base):
    id = Column(String(20), primary_key=True) 
    skill_name = Column(String(50), nullable=False)
    deleted = Column(Boolean, nullable=False)

    