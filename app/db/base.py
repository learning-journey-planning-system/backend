# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.course import Course
from app.models.courseskill import CourseSkill
from app.models.jobrole import JobRole
from app.models.jobroleskill import JobRoleSkill
from app.models.learningjourney import LearningJourney
from app.models.registration import Registration
from app.models.role import Role
from app.models.selection import Selection
from app.models.skill import Skill
from app.models.staff import Staff

