from .msg import Msg

from .course import Course, CourseCreate, CourseUpdate, CourseWithSkills, CourseWithCompletionStatus
from .jobrole import JobRole, JobRoleCreate, JobRoleUpdate, JobRoleWithSkills, JobRoleWithSkillsWithCourses
from .learningjourney import LearningJourney, LearningJourneyCreate, LearningJourneyUpdate, LearningJourneyFull, LearningJourneyFullWithSkills, LearningJourneyWithCourses
from .registration import Registration, RegistrationCreate, RegistrationUpdate
from .role import Role, RoleCreate, RoleUpdate
from .skill import Skill, SkillCreate, SkillUpdate, SkillWithCourses
from .staff import Staff, StaffCreate, StaffUpdate
