from typing import Optional

from pydantic import BaseModel

from .staff import Staff
from .jobrole import JobRole

# Shared properties
class LearningJourneyBase(BaseModel):
    staff_id: Optional[int] = None
    jobrole_id: Optional[int] = None

# Properties to receive via API on creation
class LearningJourneyCreate(LearningJourneyBase):
    staff_id: int
    jobrole_id: int

# Properties to receive via API on update
class LearningJourneyUpdate(LearningJourneyBase):
    pass

# Properties shared by models stored in DB
class LearningJourneyInDBBase(LearningJourneyBase):
    id: int
    staff: Staff
    jobrole: JobRole

    class Config:
        orm_mode = True

# Properties to return via API
class LearningJourney(LearningJourneyInDBBase):
    pass

# # Additional properties to return via API
# class LearningJourneyInDB(LearningJourneyInDBBase):