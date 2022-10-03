from app.crud.base import CRUDBase
from app.models.skill import Skill
from app.schemas.skill import SkillCreate, SkillUpdate

skill = CRUDBase[Skill, SkillCreate, SkillUpdate](Skill)