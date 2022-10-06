from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.LearningJourney])
def read_learningjourneys(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve learning journeys.
    """
    learningjourneys = crud.learningjourney.get_multi(db)
    return learningjourneys


@router.post("/", response_model=schemas.LearningJourney)
def create_learningjourney(
    *,
    db: Session = Depends(deps.get_db),
    learningjourney_in: schemas.LearningJourneyCreate
) -> Any:
    """
    Create new learning journey.
    """
    learningjourney = crud.learningjourney.get_learning_journey_by_create_obj(db, obj_in=learningjourney_in)
    if learningjourney:
        raise HTTPException(
            status_code=400,
            detail="The learning journey with this staff_id and jobrole_id already exists in the system.",
        )
    learningjourney = crud.learningjourney.create(db=db, obj_in=learningjourney_in)
    return learningjourney


@router.get("/{learningjourney_id}", response_model=schemas.LearningJourneyFullWithSkills)
def read_learningjourney(
    *,
    db: Session = Depends(deps.get_db),
    learningjourney_id: int
) -> Any:
    """
    Get learning journey by ID.
    For SC20 View learning journey.
    """
    learningjourney = crud.learningjourney.get(db=db, id=learningjourney_id)
    if not learningjourney:
        raise HTTPException(status_code=404, detail="Learning Journey not found")
    return learningjourney


@router.put("/{learningjourney_id}", response_model=schemas.LearningJourney)
def update_learningjourney(
    *,
    db: Session = Depends(deps.get_db),
    learningjourney_id: int,
    learningjourney_in: schemas.LearningJourneyUpdate
) -> Any:
    """
    Update a learning journey.
    """
    learningjourney = crud.learningjourney.get(db=db, id=learningjourney_id)
    if not learningjourney:
        raise HTTPException(status_code=404, detail="Learning Journey not found")
    learningjourney = crud.learningjourney.update(db=db, db_obj=learningjourney, obj_in=learningjourney_in)
    return learningjourney


@router.delete("/{learningjourney_id}", response_model=List[schemas.LearningJourney])
def delete_learningjourney(
    *,
    db: Session = Depends(deps.get_db),
    learningjourney_id: int
) -> Any:
    """
    Delete a learning journey.
    """
    learningjourney = crud.learningjourney.get(db=db, id=learningjourney_id)
    if not learningjourney:
        raise HTTPException(status_code=404, detail="Learning Journey not found")
    remaining_learningjourneys = crud.learningjourney.remove(db=db, id=learningjourney_id)
    return remaining_learningjourneys