from .base import CRUDBase
from app.models.jobroleskill import JobRoleSkill
from app.schemas.jobroleskill import JobRoleSkillCreate, JobRoleSkillUpdate

jobroleskill = CRUDBase[JobRoleSkill, JobRoleSkillCreate, JobRoleSkillUpdate](JobRoleSkill)