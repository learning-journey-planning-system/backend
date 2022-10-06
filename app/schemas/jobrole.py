from typing import Optional, List

from pydantic import BaseModel
from .skill import Skill

# Shared properties
class JobRoleBase(BaseModel):
    jobrole_name: Optional[str] = None
    deleted: Optional[bool] = None

# Properties to receive via API on creation
class JobRoleCreate(JobRoleBase):
    id: int # need to change to auto increment

# Properties to receive via API on update
class JobRoleUpdate(JobRoleBase):
    pass

# Properties shared by models stored in DB
class JobRoleInDBBase(JobRoleBase):
    pass

    class Config:
        orm_mode = True

# Properties to return via API
class JobRole(JobRoleInDBBase):
    id: int

# Additional properties to return via API
class JobRoleWithSkills(JobRoleInDBBase):
    skills: List[Skill] = []