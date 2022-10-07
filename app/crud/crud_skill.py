from typing import Optional

from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.skill import Skill
from app.schemas.skill import SkillCreate, SkillUpdate

class CRUDSkill(CRUDBase[Skill, SkillCreate, SkillUpdate]):

    # update skill to deleted
    def remove(self, db: Session, *, id: int) -> Optional[Skill]:
        skill = db.query(Skill).filter(Skill.id == id).first()
        setattr(skill, 'deleted', True)
        db.commit()
        db.refresh(skill)
        return db.query(Skill).all()

skill = CRUDSkill(Skill)