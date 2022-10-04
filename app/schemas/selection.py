from typing import Optional

from pydantic import BaseModel

from .learningjourney import LearningJourney
from .course import Course

# Shared properties
class SelectionBase(BaseModel):
    learningjourney_id: Optional[int] = None
    course_id: Optional[str] = None

# Properties to receive via API on creation
class SelectionCreate(SelectionBase):
    learningjourney_id: int
    course_id: str

# Properties to receive via API on update
class SelectionUpdate(SelectionBase):
    pass

# Properties shared by models stored in DB
class SelectionInDBBase(SelectionBase):
    learningjourney: Optional[LearningJourney] = None
    course: Optional[Course] = None

    class Config:
        orm_mode = True

# Properties to return via API
class Selection(SelectionInDBBase):
    pass

# # Additional properties to return via API
# class SelectionInDB(SelectionInDBBase):