from typing import Optional, List
from .base import CRUDBase
from sqlalchemy.orm import Session
from app.models.jobrole import JobRole
from app.schemas.jobrole import JobRoleCreate, JobRoleUpdate

class CRUDJobRole(CRUDBase[JobRole, JobRoleCreate, JobRoleUpdate]):

    # update jobrole to deleted
    def delete(self, db: Session, *, jobrole_id: int) -> Optional[JobRole]:
        jobrole = db.query(self.model).get({"jobrole_id":jobrole_id})
        setattr(jobrole, 'deleted', True)
        return db.query(self.model).all()

    def get_jobrole(self, db: Session, *, jobrole_id: int) -> List[JobRole]:
        return db.query(JobRole).filter(JobRole.id == jobrole_id).all()

jobrole = CRUDJobRole(JobRole)