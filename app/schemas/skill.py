from typing import Optional

from pydantic import BaseModel

# Shared properties
class SkillBase(BaseModel):
    skill_name: Optional[str] = None

# Properties to receive via API on creation
class SkillCreate(SkillBase):
    id: str
    skill_name: str
    deleted: bool

# Properties to receive via API on update
class SkillUpdate(SkillBase):
    skill_name: str


# Properties to receive via API on delete
class SkillDelete(SkillBase):
    deleted: bool


# Properties shared by models stored in DB
class SkillInDBBase(SkillBase):
    pass

    class Config:
        orm_mode = True

# Properties to return via API
class Skill(SkillInDBBase):
    id: str
    skill_name: str
    deleted: bool
