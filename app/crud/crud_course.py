from typing import List

from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseUpdate


class CRUDCourse(CRUDBase[Course, CourseCreate, CourseUpdate]):

    def get_course(self, db: Session, *, course_id: str) -> List[Course]:
        return db.query(Course).filter(Course.id == course_id).all()   

course = CRUDCourse(Course)