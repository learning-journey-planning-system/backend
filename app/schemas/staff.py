from typing import Optional

from pydantic import BaseModel, EmailStr

# Shared properties
class StaffBase(BaseModel):
    staff_fname: Optional[str] = None
    staff_lname: Optional[str] = None
    dept: Optional[str] = None
    email: Optional[EmailStr] = None
    role_id: Optional[int] = None

# Properties to receive via API on creation
class StaffCreate(StaffBase):
    id: int
    staff_fname: str
    staff_lname: str
    dept: str
    email: EmailStr
    role_id: int

# Properties to receive via API on update
class StaffUpdate(StaffBase):
    pass

# Properties shared by models stored in DB
class StaffInDBBase(StaffBase):
    id: int

    class Config:
        orm_mode = True

# Properties to return via API
class Staff(StaffInDBBase):
    pass
    