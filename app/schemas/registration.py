from typing import Optional

from pydantic import BaseModel

# Shared properties
class RegistrationBase(BaseModel):
    reg_status: Optional[str] = None
    completion_status: Optional[str] = None
    staff_id: Optional[int] = None
    course_id: Optional[str] = None

# Properties to receive via API on creation
class RegistrationCreate(RegistrationBase):
    id: int
    reg_status: str
    completion_status: str
    staff_id: int
    course_id: str

# Properties to receive via API on update
class RegistrationUpdate(RegistrationBase):
    pass

# Properties shared by models stored in DB
class RegistrationInDBBase(RegistrationBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

# Properties to return via API
class Registration(RegistrationInDBBase):
    pass
    