# to add more specialised CRUD methods that are not in the base class

from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.staff import Staff
from app.schemas.staff import StaffCreate, StaffUpdate


class CRUDStaff(CRUDBase[Staff, StaffCreate, StaffUpdate]):

    # example
    def get_by_email(self, db: Session, *, email: str) -> Optional[Staff]:
        return db.query(Staff).filter(Staff.email == email).first()

staff = CRUDStaff(Staff)