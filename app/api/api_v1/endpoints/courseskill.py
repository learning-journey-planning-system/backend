from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Courseskill])
def read_courseskill(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve courseskill.
    """
    courseskills = crud.courseskill.get_multi(db)
    return courseskills


@router.post("/", response_model=schemas.Courseskill)
def create_courseskill(
    *,
    db: Session = Depends(deps.get_db),
    courseskill_in: schemas.CourseskillCreate
) -> Any:
    """
    Create new Courseskill.
    """
    courseskill = crud.courseskill.get(db, id=courseskill_in.id)
    if courseskill:
        raise HTTPException(
            status_code=400,
            detail="The course with this skill id already exists in the system.",
        )
    courseskill = crud.courseskill.create(db, obj_in=courseskill_in)
    return courseskill


@router.get("/{skill_id}", response_model=schemas.Courseskill)
def read_courseskill(
    *,
    db: Session = Depends(deps.get_db),
    skill_id: int
) -> Any:
    """
    Get courseskill by ID.
    """
    courseskill = crud.courseskill.get(db=db, id=skill_id)
    if not courseskill:
        raise HTTPException(status_code=404, detail="courseskill not found")
    return courseskill


@router.put("/{skill_id}", response_model=schemas.Courseskill)
def update_courseskill(
    *,
    db: Session = Depends(deps.get_db),
    skill_id: int,
    courseskill_in: schemas.CourseskillUpdate
) -> Any:
    """
    Update a courseskill.
    """
    courseskill = crud.courseskill.get(db, id=skill_id)
    if not courseskill:
        raise HTTPException(
            status_code=404,
            detail="The Course with this skill_id does not exist in the system",
        )
    courseskill = crud.courseskill.update(db, db_obj=courseskill, obj_in=courseskill_in)
    return courseskill


@router.delete("/{skill_id}", response_model=List[schemas.Courseskill])
def delete_courseskill(
    *,
    db: Session = Depends(deps.get_db),
    skill_id: int
) -> Any:
    """
    Delete a courseskill.
    """
    courseskill = crud.courseskill.get(db=db, id=skill_id)
    if not courseskill:
        raise HTTPException(status_code=404, detail="Skill not found")
    remaining_courseskill = crud.courseskill.remove(db=db, id=skill_id)
    return remaining_courseskill