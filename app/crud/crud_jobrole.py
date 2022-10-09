from typing import Optional, List

from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.jobrole import JobRole
from app.schemas.jobrole import JobRoleCreate, JobRoleUpdate

class CRUDJobRole(CRUDBase[JobRole, JobRoleCreate, JobRoleUpdate]):

    # get jobrole by jobrole_name
    def get_by_jobrole_name(self, db: Session, *, jobrole_name: str) -> Optional[JobRole]:
        return db.query(JobRole).filter(JobRole.jobrole_name == jobrole_name).first()

    # update jobrole to deleted
    def remove(self, db: Session, *, id: int) -> JobRole:
        jobrole = db.query(JobRole).filter(JobRole.id == id).first()
        setattr(jobrole, 'deleted', True)
        db.commit()
        db.refresh(jobrole)
        return jobrole

    def get_multi_available(self, db: Session) -> List[JobRole]:
        return db.query(JobRole).filter(JobRole.deleted == False).all()

jobrole = CRUDJobRole(JobRole)