from typing import Optional

from pydantic import BaseModel, EmailStr
from .skill import Skill
from .jobrole import Jobrole

# Shared properties
class JobroleskillBase(BaseModel):
    id: int
    skillid: str

# Properties to receive via API on creation
class JobroleskillCreate(JobroleskillBase):
    # Need to provide minimally jobrole id and skill id on jobrole skill creation
    id: int 
    skillid: str 

# Properties to receive via API on update
class JobroleskillUpdate(JobroleskillBase):
    id: Optional[int] = None

# Properties shared by models stored in DB
class JobroleskillInDBBase(JobroleskillBase):
    skill: Optional[Skill] = None
    jobrole: Optional[Jobrole] = None

    class Config:
        orm_mode = True

# Properties to return via API
class Jobroleskill(JobroleskillInDBBase):
    id: Optional[int] = None
    skillid: Optional[str] = None
