from typing import Optional, List

from pydantic import BaseModel
from .course import Course

# Shared properties
class SkillBase(BaseModel):
    skill_name: Optional[str] = None
    deleted: Optional[bool] = False

# Properties to receive via API on creation
class SkillCreate(SkillBase):
    id: str
    skill_name: str
    deleted: bool

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
    id: str

class SkillWithCourses(SkillInDBBase):
    courses: List[Course] = []