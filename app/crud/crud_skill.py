from typing import Optional, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.skill import Skill
from app.schemas.skill import SkillCreate, SkillUpdate

class CRUDSkill(CRUDBase[Skill, SkillCreate, SkillUpdate]):

    # update skill to deleted
    def delete(self, db: Session, *, skill_id: int) -> Optional[Skill]:
        skill = db.query(self.model).get(skill_id)
        setattr(skill, 'deleted', True)
        return db.query(self.model).all()
    
    def get_skill_id(self, db: Session, *, skill_id: str) -> List[Skill]:
        return db.query(Skill).filter(Skill.id == skill_id).all()

skill = CRUDSkill(Skill)