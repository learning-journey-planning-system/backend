from typing import Optional, List

from pydantic import BaseModel

# Shared properties
class JobRoleBase(BaseModel):
    jobrole_name: Optional[str] = None

# Properties to receive via API on creation
class JobRoleCreate(JobRoleBase):
    jobrole_name: str # required

# Properties to receive via API on update
class JobRoleUpdate(JobRoleBase):
    pass

# Properties shared by models stored in DB
class JobRoleInDBBase(JobRoleBase):
    id: int
    deleted: Optional[bool] = False

    class Config:
        orm_mode = True

# Properties to return via API
class JobRole(JobRoleInDBBase):
    pass

# Additional properties to return via API
from .skill import Skill, SkillWithCourses
class JobRoleWithSkills(JobRole):
    skills: List[Skill] = []

class JobRoleWithSkillsWithCourses(JobRole):
    skills: List[SkillWithCourses] = []