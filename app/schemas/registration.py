from typing import Optional

from pydantic import BaseModel, EmailStr
from .staff import Staff
from .course import Course

# Shared properties
class StaffBase(BaseModel):
    course_id: Optional[str] = None
    staff_id: Optional[int] = None
    reg_status: Optional[str] = None
    completion_status: Optional[str] = None

# Properties to receive via API on creation
class StaffCreate(StaffBase):
    # Need to provide minimally staff_id and password on staff creation
    id: int # since we will be getting this from LMS, we do not need to autogenerate it

# Properties to receive via API on update
class StaffUpdate(StaffBase):
    pass

# Properties shared by models stored in DB
class StaffInDBBase(StaffBase):
    id: Optional[int] = None
    course: Optional[Course] = None
    staff: Optional[Staff] = None

    class Config:
        orm_mode = True

# Properties to return via API
class Staff(StaffInDBBase):
    pass

# Additional properties to return via API
# @dataclass
# class StaffInDB(StaffInDBBase):
    