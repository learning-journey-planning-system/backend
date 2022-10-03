from typing import Optional

from pydantic import BaseModel, EmailStr

# Shared properties
class CourseBase(BaseModel):
    course_name: Optional[str] = None
    

# Properties to receive via API on creation
class CourseCreate(CourseBase):
    pass

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
    course_name : str
    course_status : str # Active or Retired
    course_type : str # Internal or External 
    course_category : str 
    deleted : bool
    


    