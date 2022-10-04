from .base import CRUDBase
from app.models.courseskill import CourseSkill
from app.schemas.courseskill import CourseSkillCreate, CourseSkillUpdate

courseskill = CRUDBase[CourseSkill, CourseSkillCreate, CourseSkillUpdate](CourseSkill)
