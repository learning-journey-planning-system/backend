from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import learningjourney
from app.models.learningjourney import LearningJourney
from app.schemas.learningjourney import LearningJourneyCreate, LearningJourneyUpdate


class CRUDLearningJourney(CRUDBase[LearningJourney, LearningJourneyCreate, LearningJourneyUpdate]):

    def get_learning_journeys_by_staff_id(self, db: Session, *, staff_id: int) -> List[LearningJourney]:
        return db.query(LearningJourney).filter(LearningJourney.staff_id == staff_id).all()

learningjourney = CRUDLearningJourney(LearningJourney)