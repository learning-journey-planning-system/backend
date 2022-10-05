from typing import Optional, List

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.selection import Selection
from app.schemas.selection import SelectionCreate, SelectionUpdate


class CRUDSelection(CRUDBase[Selection, SelectionCreate, SelectionUpdate]):

    def get(self, db: Session, learningjourney_id:int, course_id: str) -> Optional[Selection]:
        return db.query(Selection).filter(
            Selection.learningjourney_id == learningjourney_id, 
            Selection.course_id == course_id
            ).first()

    def remove(self, db: Session, *, learningjourney_id:int, course_id: str) -> List[Selection]:
        obj = self.get(db=db, learningjourney_id=learningjourney_id, course_id=course_id)
        db.delete(obj)
        db.commit()
        return db.query(Selection).all()
        
    def get_selections_by_learningjourney_id(self, db: Session, learningjourney_id:int) -> List[Selection]:
        return db.query(Selection).filter(Selection.learningjourney_id == learningjourney_id).all()


    def get_selections_by_learningjourney_id(self, db: Session, learningjourney_id:int) -> List[Selection]:
        return db.query(Selection).filter(Selection.learningjourney_id == learningjourney_id).all()

selection = CRUDSelection(Selection)