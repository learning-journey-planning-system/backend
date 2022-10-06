from typing import Optional

from pydantic import BaseModel

# Shared properties
class RoleBase(BaseModel):
    role_name: Optional[str] = None

# Properties to receive via API on creation
class RoleCreate(RoleBase):
    id: int
    role_name: str # required

# Properties to receive via API on update
class RoleUpdate(RoleBase):
    pass

# Properties shared by models stored in DB
class RoleInDBBase(RoleBase):
    id: int

    class Config:
        orm_mode = True

# Properties to return via API
class Role(RoleInDBBase):
    pass
