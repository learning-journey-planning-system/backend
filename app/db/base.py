# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base
from app.models.course import Course
from app.models.jobrole import JobRole
from app.models.learningjourney import LearningJourney
from app.models.registration import Registration
from app.models.role import Role
from app.models._secondary import Course_Skill, JobRole_Skill, Course_LearningJourney
from app.models.skill import Skill
from app.models.staff import Staff

