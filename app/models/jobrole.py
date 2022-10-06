from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class JobRole(Base):
    id = Column(Integer, primary_key=True)
    jobrole_name = Column(String(20), nullable=False)
    deleted = Column(Boolean, default = False)

    # one jobrole can have many learning journeys
    learningjourneys = relationship("LearningJourney", back_populates="jobrole")

    # one jobrole can have many skills
    skills = relationship("Skill", back_populates="jobroles", secondary="jobrole_skill")

    
