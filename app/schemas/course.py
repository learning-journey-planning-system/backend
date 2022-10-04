from typing import Optional

from pydantic import BaseModel, EmailStr

# Shared properties
class CourseBase(BaseModel):
    course_name: Optional[str] = None
    course_desc : Optional[str] = None
    course_status : Optional[str] = None # Active or Retired
    course_type : Optional[str] = None # Internal or External 
    course_category : Optional[str] = None 
    

# Properties to receive via API on creation
class CourseCreate(CourseBase):
    id : str

# Properties to receive via API on update
class CourseUpdate(CourseBase):
    pass

# Properties shared by models stored in DB
class CourseInDBBase(CourseBase):
    pass

    class Config:
        orm_mode = True

# Properties to return via API
class Course(CourseInDBBase):
    id : str
    


    