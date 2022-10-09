from typing import Optional, List

from pydantic import BaseModel

# Shared properties
class SkillBase(BaseModel):
    skill_name: Optional[str] = None

# Properties to receive via API on creation
class SkillCreate(SkillBase):
    skill_name: str

# Properties to receive via API on update
class SkillUpdate(SkillBase):
    pass

# Properties shared by models stored in DB
class SkillInDBBase(SkillBase):
    id : int
    deleted: Optional[bool] = False

    class Config:
        orm_mode = True

# Properties to return via API
class Skill(SkillInDBBase):
    pass

# Additional properties to return via API
from .course import Course
class SkillWithCourses(Skill):
    courses: List[Course] = []