from app.crud.base import CRUDBase
from app.models.skill import Skill
from app.schemas.skill import SkillCreate, SkillUpdate, SkillDelete

skill = CRUDBase[Skill, SkillCreate, SkillUpdate, SkillDelete](Skill)