from typing import Optional, List

from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.jobrole import JobRole
from app.schemas.jobrole import JobRoleCreate, JobRoleUpdate

class CRUDJobRole(CRUDBase[JobRole, JobRoleCreate, JobRoleUpdate]):

    # update jobrole to deleted
    def delete(self, db: Session, *, jobrole_id: int) -> Optional[JobRole]:
        jobrole = db.query(self.model).get({"jobrole_id":jobrole_id})
        setattr(jobrole, 'deleted', True)
        return db.query(self.model).all()

    def get_multi_available(self, db: Session) -> List[JobRole]:
        return db.query(self.model).filter(self.model.deleted == False).all()

jobrole = CRUDJobRole(JobRole)