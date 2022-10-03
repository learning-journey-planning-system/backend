from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Jobroleskill])
def read_jobroleskills(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve Jobroleskills.
    """
    jobroleskills = crud.jobroleskill.get_multi(db)
    return jobroleskills


@router.post("/", response_model=schemas.Jobroleskill)
def create_jobroleskill(
    *,
    db: Session = Depends(deps.get_db),
    jobroleskill_in: schemas.JobroleskillCreate
) -> Any:
    """
    Create new jobroleskill.
    """
    jobroleskill = crud.jobroleskill.get(db, id=jobroleskill_in.id)
    if jobroleskill:
        raise HTTPException(
            status_code=400,
            detail="The skill with this jobrole id already exists in the system.",
        )
    jobroleskill = crud.jobroleskill.create(db=db, obj_in=jobroleskill_in)
    return jobroleskill


@router.get("/{jobrole_id}", response_model=schemas.Jobroleskill)
def read_jobroleskill(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int
) -> Any:
    """
    Get jobroleskill by ID.
    """
    jobroleskill = crud.jobroleskill.get(db=db, id=jobrole_id)
    if not jobroleskill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return jobroleskill


@router.put("/{jobrole_id}", response_model=schemas.Jobroleskill)
def update_jobroleskill(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int,
    jobroleskill_in: schemas.JobroleskillUpdate
) -> Any:
    """
    Update an Jobroleskill.
    """
    jobroleskill = crud.jobroleskill.get(db=db, id=jobrole_id)
    if not jobroleskill:
        raise HTTPException(status_code=404, detail="Skill not found")
    jobroleskill = crud.jobroleskill.update(db=db, db_obj=jobroleskill, obj_in=jobroleskill_in)
    return jobroleskill


@router.delete("/{jobrole_id}", response_model=List[schemas.Jobroleskill])
def delete_jobroleskill(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int
) -> Any:
    """
    Delete an jobroleskill.
    """
    jobroleskill = crud.jobroleskill.get(db=db, id=jobrole_id)
    if not jobroleskill:
        raise HTTPException(status_code=404, detail="Skill not found")
    remaining_jobroleskill = crud.jobroleskill.remove(db=db, id=jobrole_id)
    return remaining_jobroleskill
