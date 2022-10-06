from typing import List

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.learningjourney import LearningJourney
from app.schemas.learningjourney import LearningJourneyCreate, LearningJourneyUpdate

class CRUDLearningJourney(CRUDBase[LearningJourney, LearningJourneyCreate, LearningJourneyUpdate]):

    def get_learning_journey_by_staff_id_and_jobrole_id(self, db: Session, *, obj_in = LearningJourneyCreate) -> LearningJourney:
        return (db.query(LearningJourney)
        .filter(LearningJourney.staff_id == obj_in.staff_id,
                LearningJourney.jobrole_id == obj_in.jobrole_id)
        .first())

    # def get_learning_journeys_by_staff_id(self, db: Session, *, staff_id: int) -> List[LearningJourney]:
    #     return db.query(LearningJourney).filter(LearningJourney.staff_id == staff_id).all()

learningjourney = CRUDLearningJourney(LearningJourney)