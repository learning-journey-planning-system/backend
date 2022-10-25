from typing import List

from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.registration import Registration
from app.schemas.registration import RegistrationCreate, RegistrationUpdate


class CRUDRegistration(CRUDBase[Registration, RegistrationCreate, RegistrationUpdate]):

    def get_registration_by_staff_id(self, db: Session, *, staff_id: int) -> List[Registration]:
        return db.query(Registration).filter(Registration.staff_id == staff_id).all()

    
    def get_registration_by_staff_and_course_id(self, db: Session, *, staff_id: int, course_id: str) -> Registration:
        return db.query(Registration).filter(Registration.staff_id == staff_id, Registration.course_id == course_id).first()

    def get_completion_status(self, reg_status: str, completion_status: str) -> str:
        if reg_status == "Registered":
            return completion_status
        else:
            return "Registration " + reg_status

registration = CRUDRegistration(Registration)