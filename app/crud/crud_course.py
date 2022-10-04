from app.crud.base import CRUDBase
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseUpdate

course = CRUDBase[Course, CourseCreate, CourseUpdate](Course)