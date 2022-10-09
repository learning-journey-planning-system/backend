from typing import Optional, List

from pydantic import BaseModel

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

    class Config:
        orm_mode = True

# Properties to return via API
class LearningJourney(LearningJourneyInDBBase):
    pass

# Additional properties to return via API
from .staff import Staff
from .jobrole import JobRole
from .course import Course
class LearningJourneyFull(LearningJourney):
    staff: Staff
    jobrole: JobRole
    courses: List[Course] = []

from .course import CourseWithSkills
class LearningJourneyFullWithSkills(LearningJourneyFull):
    courses: List[CourseWithSkills] = []

class LearningJourneyWithCourses(LearningJourney):
    courses: List[Course] = []