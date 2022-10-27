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

    completion_status = crud.registration.get_completion_status(reg_status=registration.reg_status, completion_status=registration.completion_status)
    
    return {"msg": completion_status}

@router.get("{staff_id}/acquired_skills", response_model=List[schemas.Skill])
def get_acquired_skill_for_jobrole(
    *,
    db: Session = Depends(deps.get_db),
    staff_id: int,
    jobrole_id: int
) -> Any:
    """
    Get Acquired Skills For A JobRole.
    SC23 View acquired skills of job role by learner. 
    """

    # Check if staff exist
    staff = crud.staff.get(db, id=staff_id)
    if not staff:
        raise HTTPException(status_code=404,detail="The staff with this staff_id does not exist in the system")

    # Check if the jobrole exists
    jobrole = crud.jobrole.get(db, id=jobrole_id)
    if not jobrole:
        raise HTTPException(status_code=404,detail="The jobrole with this jobrole_id does not exist in the system")

    # Check if the jobrole has not been soft deleted
    if jobrole.deleted:
        raise HTTPException(status_code=404,detail="The jobrole with this jobrole_id has been soft deleted")
    
    # Check for registrations
    registrations = staff.registrations
    if not registrations:
        raise HTTPException(status_code=404, detail="No registrations found for this staff_id")
    

    # Check for completed course in registrations
    course_ids = [registration.course_id for registration in registrations if (registration.reg_status == "Registered" and registration.completion_status == "Completed")]
    if not course_ids:
        raise HTTPException(status_code=404, detail="No completed courses found for this staff_id")

    courses = [crud.course.get(db=db, id=id) for id in course_ids]
    acquired_skills = [skill for course in courses for skill in course.skills if (skill in jobrole.skills)]

    if not acquired_skills:
        raise HTTPException(status_code=404, detail="No skills acquired for this jobrole_id")

    skill = list(set(acquired_skills))

    return skill