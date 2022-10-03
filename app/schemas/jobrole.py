from typing import Optional

from pydantic import BaseModel

# Shared properties
class JobroleBase(BaseModel):
    jobrole_name: Optional[str] = None

# Properties to receive via API on creation
class JobroleCreate(JobroleBase):
    id: int

# Properties to receive via API on update
class JobroleUpdate(JobroleBase):
    pass

# Properties shared by models stored in DB
class JobroleInDBBase(JobroleBase):
    pass

    class Config:
        orm_mode = True

# Properties to return via API
class Jobrole(JobroleInDBBase):
    id: int
