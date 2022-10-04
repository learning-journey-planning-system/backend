from typing import Optional

from pydantic import BaseModel, EmailStr
from .skill import Skill
from .jobrole import JobRole

# Shared properties
class JobRoleSkillBase(BaseModel):
    jobrole_id: int
    skill_id: str

# Properties to receive via API on creation
class JobRoleSkillCreate(JobRoleSkillBase):
    pass

# Properties to receive via API on update
class JobRoleSkillUpdate(JobRoleSkillBase):
    pass

# Properties shared by models stored in DB
class JobRoleSkillInDBBase(JobRoleSkillBase):
    skill: Optional[Skill] = None
    jobrole: Optional[JobRole] = None

    class Config:
        orm_mode = True

# Properties to return via API
class JobRoleSkill(JobRoleSkillInDBBase):
    pass
