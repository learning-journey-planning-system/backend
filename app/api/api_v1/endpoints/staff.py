from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Staff])
def read_staffs(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve staffs.
    """
    staffs = crud.staff.get_multi(db)
    return staffs


@router.post("/", response_model=schemas.Staff)
def create_staff(
    *,
    db: Session = Depends(deps.get_db),
    staff_in: schemas.StaffCreate
) -> Any:
    """
    Create new staff.
    """
    staff = crud.staff.get(db, id=staff_in.id)
    if staff:
        raise HTTPException(
            status_code=400,
            detail="The staff with this staff id already exists in the system.",
        )
    staff = crud.staff.create(db, obj_in=staff_in)
    return staff


@router.get("/{staff_id}", response_model=schemas.Staff)
def read_staff(
    *,
    db: Session = Depends(deps.get_db),
    staff_id: int
) -> Any:
    """
    Get staff by ID.
    """
    staff = crud.staff.get(db=db, id=staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff


@router.put("/{staff_id}", response_model=schemas.Staff)
def update_staff(
    *,
    db: Session = Depends(deps.get_db),
    staff_id: int,
    staff_in: schemas.StaffUpdate
) -> Any:
    """
    Update a staff.
    """
    staff = crud.staff.get(db, id=staff_id)
    if not staff:
        raise HTTPException(
            status_code=404,
            detail="The staff with this staff_id does not exist in the system",
        )
    staff = crud.staff.update(db, db_obj=staff, obj_in=staff_in)
    return staff


@router.delete("/{staff_id}", response_model=List[schemas.Staff])
def delete_staff(
    *,
    db: Session = Depends(deps.get_db),
    staff_id: int
) -> Any:
    """
    Delete a staff.
    """
    staff = crud.staff.get(db=db, id=staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")

    #Remove staff's learning journeys and resgistration
    registrations = staff.registrations
    learningjourneys = staff.learningjourneys

    if registrations != []:
        for registration in registrations:
            crud.registration.remove(db=db, id=registration.id)

    if learningjourneys != []:
        for learningjourney in learningjourneys:
            crud.learningjourney.remove(db=db, id=learningjourney.id)

    remaining_staffs = crud.staff.remove(db=db, id=staff_id)

    return remaining_staffs


@router.get("/{staff_id}/learningjourneys", response_model=List[schemas.LearningJourneyFullWithSkills])
def read_staff_learning_journeys(
    *,
    db: Session = Depends(deps.get_db),
    staff_id: int
) -> Any:
    """
    Get all the learning journeys that a staff has.
    For SC20 View Learning Journey by learner.
    """
    staff = crud.staff.get(db=db, id=staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff.learningjourneys


@router.get("/{staff_id}/courses/{course_id}/completion_status", response_model=schemas.Msg)
def get_completion_status(
    *,
    db: Session = Depends(deps.get_db),
    staff_id: int,
    course_id: str
) -> Any:
    """
    Get completion status of a course for a staff.
    Returns one of these options: (1) Not Registered, (2) Registration Rejected, (3) Registration Waitlist, (4) Ongoing, (5) Completed
    """
    registration = crud.registration.get_registration_by_staff_and_course_id(db, staff_id=staff_id, course_id=course_id)

    if registration is None:
        return {"msg": "Not Registered"}
    
    if registration.reg_status == "Registered":
        return {"msg": registration.completion_status}
    
    return {"msg": "Registration " + registration.reg_status}

