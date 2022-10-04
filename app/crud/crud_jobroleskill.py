from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.jobroleskill import JobRoleSkill
from app.schemas.jobroleskill import JobRoleSkillCreate, JobRoleSkillUpdate


class CRUDJobRoleSkill(CRUDBase[JobRoleSkill, JobRoleSkillCreate, JobRoleSkillUpdate]):

    #Get Skill from Jobrole
    def get(self, db: Session, jobrole_id: int, skill_id: str) -> Optional[JobRoleSkill]:
            return (db.query(self.model)
            .filter(self.model.jobrole_id == jobrole_id)
            .filter(self.model.skill_id == skill_id)
            .first()
        )

    def remove(self, db: Session, *, jobrole_id: int, skill_id: str) -> List[JobRoleSkill]:
                obj = db.query(self.model).get({"jobrole_id":jobrole_id, "skill_id":skill_id})
                db.delete(obj)
                db.commit()
                return db.query(self.model).all()        

jobroleskill = CRUDJobRoleSkill(JobRoleSkill)