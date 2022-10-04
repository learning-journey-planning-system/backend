from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import registration
from app.models.registration import Registration
from app.schemas.registration import RegistrationCreate, RegistrationUpdate


class CRUDRegistration(CRUDBase[Registration, RegistrationCreate, RegistrationUpdate]):

    def get_registration_by_staff_id(self, db: Session, *, staff_id: int) -> List[Registration]:
        return db.query(Registration).filter(Registration.staff_id == staff_id).all()

registration = CRUDRegistration(Registration)