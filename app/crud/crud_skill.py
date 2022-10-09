from typing import Optional

from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.skill import Skill
from app.schemas.skill import SkillCreate, SkillUpdate

class CRUDSkill(CRUDBase[Skill, SkillCreate, SkillUpdate]):

    # get skill by skill_name
    def get_by_skill_name(self, db: Session, *, skill_name: str) -> Optional[Skill]:
        return db.query(Skill).filter(Skill.skill_name == skill_name).first()

    # update skill to deleted
    def remove(self, db: Session, *, id: int) -> Skill:
        skill = db.query(Skill).filter(Skill.id == id).first()
        setattr(skill, 'deleted', True)
        db.commit()
        db.refresh(skill)
        return skill

skill = CRUDSkill(Skill)