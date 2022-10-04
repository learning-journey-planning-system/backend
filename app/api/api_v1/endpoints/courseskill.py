from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.CourseSkill])
def read_courseskill(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve courseskills.
    """
    courseskills = crud.courseskill.get_multi(db)
    return courseskills


@router.post("/", response_model=schemas.CourseSkill)
def create_courseskill(
    *,
    db: Session = Depends(deps.get_db),
    courseskill_in: schemas.CourseSkillCreate
) -> Any:
    """
    Create new CourseSkill.
    """
    courseskill = crud.courseskill.get(db, skill_id=courseskill_in.skill_id, course_id=courseskill_in.course_id)
    if courseskill:
        raise HTTPException(
            status_code=400,
            detail="The courseskill with this skill id already exists in the system.",
        )
    courseskill = crud.courseskill.create(db, obj_in=courseskill_in)
    return courseskill


@router.get("/{skill_id}/{course_id}", response_model=schemas.CourseSkill)
def read_courseskill(
    *,
    db: Session = Depends(deps.get_db),
    skill_id: str,
    course_id: str
) -> Any:
    """
    Get courseskill by skill_id and course_id.
    """
    courseskill = crud.courseskill.get(db=db, skill_id=skill_id, course_id=course_id)
    if not courseskill:
        raise HTTPException(status_code=404, detail="CourseSkill not found")
    return courseskill


# @router.put("/{courseskill_id}", response_model=schemas.CourseSkill)
# def update_courseskill(
#     *,
#     db: Session = Depends(deps.get_db),
#     courseskill_id: int,
#     courseskill_in: schemas.CourseSkillUpdate
# ) -> Any:
#     """
#     Update a courseskill.
#     """
#     courseskill = crud.courseskill.get(db, id=courseskill_id)
#     if not courseskill:
#         raise HTTPException(
#             status_code=404,
#             detail="The Course with this skill_id does not exist in the system",
#         )
#     courseskill = crud.courseskill.update(db, db_obj=courseskill, obj_in=courseskill_in)
#     return courseskill


@router.delete("/{skill_id}/{course_id}", response_model=List[schemas.CourseSkill])
def delete_courseskill(
    *,
    db: Session = Depends(deps.get_db),
    skill_id: str,
    course_id: str
) -> Any:
    """
    Delete a courseskill.
    """
    courseskill = crud.courseskill.get(db=db, skill_id=skill_id, course_id=course_id)
    if not courseskill:
        raise HTTPException(status_code=404, detail="CourseSkill not found")
    remaining_courseskill = crud.courseskill.remove(db=db, skill_id=skill_id, course_id=course_id)
    return remaining_courseskill