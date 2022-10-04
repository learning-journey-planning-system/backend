from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import selection
from app.models.selection import Selection
from app.schemas.selection import SelectionCreate, SelectionUpdate


class CRUDSelection(CRUDBase[Selection, SelectionCreate, SelectionUpdate]):

    def get(self, db: Session, learningjourney_id: int, course_id: str) -> Optional[Selection]:
        return (db.query(selection)
        .filter(selection.learningjourney_id == learningjourney_id)
        .filter(selection.course_id == course_id)
        .first()
        )

    def remove(self, db: Session, *, learningjourney_id: int, course_id: str) -> List[Selection]:
        obj = db.query(selection).get(learningjourney_id=learningjourney_id, course_id=course_id)
        db.delete(obj)
        db.commit()
        return db.query(selection).all()

selection = CRUDSelection(Selection)