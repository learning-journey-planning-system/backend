from typing import Optional

from pydantic import BaseModel
from .skill import Skill
from .course import Course

# Shared properties
class CourseSkillBase(BaseModel):
    skill_id: str 
    course_id: str 

# Properties to receive via API on creation
class CourseSkillCreate(CourseSkillBase):
    pass

# Properties to receive via API on update
class CourseSkillUpdate(CourseSkillBase):
    pass

# Properties shared by models stored in DB
class CourseSkillInDBBase(CourseSkillBase):
    skill: Optional[Skill] = None
    course: Optional[Course] = None

    class Config:
        orm_mode = True

# Properties to return via API
class CourseSkill(CourseSkillInDBBase):
    pass
