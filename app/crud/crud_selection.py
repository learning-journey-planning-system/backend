from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.learningjourney import Selection
from app.schemas.learningjourney import SelectionCreate, SelectionUpdate


class CRUDSelection(CRUDBase[Selection, SelectionCreate, SelectionUpdate]):

    def get(self, db: Session, learningjourney_id: int, course_id: str) -> Optional[Selection]:
        return (db.query(self.model)
        .filter(self.model.learningjourney_id == learningjourney_id)
        .filter(self.model.course_id == course_id)
        .first()
        )

    def remove(self, db: Session, *, learningjourney_id: int, course_id: str) -> List[Selection]:
        obj = db.query(self.model).get(learningjourney_id, course_id)
        db.delete(obj)
        db.commit()
        return db.query(self.model).all()

staff = CRUDSelection(Selection)