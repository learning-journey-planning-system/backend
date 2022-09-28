from typing import Optional

from pydantic import BaseModel, EmailStr
from .role import Role

# Shared properties
class StaffBase(BaseModel):
    staff_fname: Optional[str] = None
    staff_lname: Optional[str] = None
    dept: Optional[str] = None
    email: Optional[EmailStr] = None
    role_id: Optional[int] = None

# Properties to receive via API on creation
class StaffCreate(StaffBase):
    # Need to provide minimally staff_id and password on staff creation
    id: int # since we will be getting this from LMS, we do not need to autogenerate it
    password: str

# Properties to receive via API on update
class StaffUpdate(StaffBase):
    password: Optional[str] = None

# Properties shared by models stored in DB
class StaffInDBBase(StaffBase):
    role: Optional[Role] = None

    class Config:
        orm_mode = True

# Properties to return via API
class Staff(StaffInDBBase):
    id: Optional[int] = None
    password: Optional[str] = None

# Additional properties to return via API
# @dataclass
# class StaffInDB(StaffInDBBase):
    