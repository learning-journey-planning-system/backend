from typing import Optional

from pydantic import BaseModel, EmailStr
from .skill import Skill
from .course import Course

# Shared properties
class CourseskillBase(BaseModel):
    id = Optional[str] = None
    courseid = Optional[str] = None

# Properties to receive via API on creation
class CourseskillCreate(CourseskillBase):
    # Need to provide minimally jobrole id and skill id on jobrole skill creation
    id: str 
    courseid: str 

# Properties to receive via API on update
class CourseskillUpdate(CourseskillBase):
    id: Optional[str] = None

# Properties shared by models stored in DB
class CourseskillInDBBase(CourseskillBase):
    skill: Optional[Skill] = None
    course: Optional[Course] = None

    class Config:
        orm_mode = True

# Properties to return via API
class Courseskill(CourseskillInDBBase):
    id: Optional[str] = None
    courseid: Optional[str] = None
