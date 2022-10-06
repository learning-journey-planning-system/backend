from typing import Optional, List

from pydantic import BaseModel

# Shared properties
class SkillBase(BaseModel):
    id : Optional[str] = None
    skill_name: Optional[str] = None
    deleted: Optional[bool] = False

# Properties to receive via API on creation
class SkillCreate(SkillBase):
    id : str
    skill_name: str

# Properties to receive via API on update
class SkillUpdate(SkillBase):
    pass

# Properties shared by models stored in DB
class SkillInDBBase(SkillBase):
    pass

    class Config:
        orm_mode = True

# Properties to return via API
class Skill(SkillInDBBase):
    pass

# Additional properties to return via API
from .course import Course
class SkillWithCourses(Skill):
    courses: List[Course] = []