from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.courseskill import CourseSkill
from app.schemas.courseskill import CourseSkillCreate, CourseSkillUpdate

class CRUDCourseSkill(CRUDBase[CourseSkill, CourseSkillCreate, CourseSkillUpdate]):

    #Get Course from Skill ID
    def get(self, db: Session, skill_id: str, course_id: str) -> Optional[CourseSkill]:
            return (db.query(self.model)
            .filter(self.model.skill_id == skill_id)
            .filter(self.model.course_id == course_id)
            .first()
        )

    def remove(self, db: Session, *, skill_id: str, course_id: str) -> List[CourseSkill]:
                obj = db.query(self.model).get({"skill_id":skill_id, "course_id":course_id})
                db.delete(obj)
                db.commit()
                return db.query(self.model).all()        


courseskill = CRUDCourseSkill(CourseSkill)