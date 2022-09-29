from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.role import RoleCreate
from app.tests.utils.user import create_random_staff
from app.tests.utils.utils import random_lower_string


def create_random_role(db: Session, *, role_id: Optional[int] = None) -> models.Role:
    if role_id is None:
        staff = create_random_staff(db)
        role_id = staff.id
    title = random_lower_string()
    description = random_lower_string()
    role_in = RoleCreate(title=title, description=description, id=id)
    return crud.role.create_with_owner(db=db, obj_in=role_in, owner_id=owner_id)
