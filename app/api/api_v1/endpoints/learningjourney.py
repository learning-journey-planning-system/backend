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
    For SC6 create a new learning journey.
    """
    learningjourney = crud.learningjourney.get_learning_journey_by_staff_id_and_jobrole_id(db, obj_in=learningjourney_in)
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


@router.post("/{learningjourney_id}/new_course/", response_model=schemas.LearningJourneyFull)
def add_course_to_learning_journey(
    *,
    db: Session = Depends(deps.get_db),
    learningjourney_id: int,
    course_id: str
) -> Any:
    """
    Add a course to a learning journey.
    For SC6 save a course to the new learning journey.
    """

    # Get the learning journey
    learningjourney = crud.learningjourney.get(db=db, id=learningjourney_id)
    if not learningjourney:
        raise HTTPException(status_code=404, detail="Learning Journey not found")
    
    # Get the course
    course = crud.course.get(db=db, id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Check if the course is already in the learning journey
    if course in learningjourney.courses:
        raise HTTPException(
            status_code=400,
            detail="The course is already in the learning journey.",
        )
    
    # Add the course to the learning journey
    learningjourney.courses.append(course)
    db.commit()
    db.refresh(learningjourney)
    return learningjourney

@router.delete("/{learningjourney_id}/delete_course/{course_id}", response_model=schemas.LearningJourneyWithCourses)
def delete_course_from_learning_journey(
    *,
    db: Session = Depends(deps.get_db),
    learningjourney_id: int,
    course_id: str
) -> Any:
    """
    Delete a course from a learning journey.
    """

    # Check if the learning journey exists
    learningjourney = crud.learningjourney.get(db=db, id=learningjourney_id)
    if not learningjourney:
        raise HTTPException(status_code=404, detail="Learning Journey not found")
    
    # Check if the course exists
    course = crud.course.get(db=db, id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Check if the course is in the learning journey
    if course not in learningjourney.courses:
        raise HTTPException(
            status_code=400,
            detail="The course is not in the learning journey.",
        )
    
    # Remove the course from the learning journey
    learningjourney.courses.remove(course)
    db.commit()
    db.refresh(learningjourney)

    return learningjourney