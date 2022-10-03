from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Course])
def read_courses(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve courses.
    """
    courses = crud.course.get_multi(db)
    return courses


@router.post("/", response_model=schemas.Course)
def create_course(
    *,
    db: Session = Depends(deps.get_db),
    course_in: schemas.StaffCreate
) -> Any:
    """
    Create new course.
    """
    course = crud.course.get(db, id=course_in.id)
    if course:
        raise HTTPException(
            status_code=400,
            detail="The course with this course id already exists in the system.",
        )
    course = crud.course.create(db, obj_in=course_in)
    return course


@router.get("/{course_id}", response_model=schemas.Course)
def read_course(
    *,
    db: Session = Depends(deps.get_db),
    course_id: int
) -> Any:
    """
    Get course by ID.
    """
    course = crud.course.get(db=db, id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail="course not found")
    return course


@router.put("/{course_id}", response_model=schemas.Course)
def update_staff(
    *,
    db: Session = Depends(deps.get_db),
   course_id: int,
    course_in: schemas.StaffUpdate
) -> Any:
    """
    Update a course.
    """
    course = crud.course.get(db, id=course_id)
    if not course:
        raise HTTPException(
            status_code=404,
            detail="The course with this course id does not exist in the system",
        )
    course = crud.course.update(db, db_obj=course, obj_in=course_in)
    return course


@router.delete("/{course_id}", response_model=List[schemas.Course])
def delete_course(
    *,
    db: Session = Depends(deps.get_db),
    course_id: int
) -> Any:
    """
    Delete a course.
    """
    course = crud.course.get(db=db, id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail="course not found")
    remaining_course = crud.skill.update(db=db, id=course_id, deleted=True)
    return remaining_course