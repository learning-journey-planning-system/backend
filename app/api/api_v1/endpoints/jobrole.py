from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.JobRole])
def read_jobroles(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve JobRoles.
    """
    jobroles = crud.jobrole.get_multi(db)
    return jobroles


@router.post("/", response_model=schemas.JobRole)
def create_jobrole(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_in: schemas.JobRoleCreate
) -> Any:
    """
    Create new jobrole.
    """
    jobrole = crud.jobrole.get(db, id=jobrole_in.id)
    if jobrole:
        raise HTTPException(
            status_code=400,
            detail="The jobrole with this jobrole id already exists in the system.",
        )
    jobrole = crud.jobrole.create(db, obj_in=jobrole_in)
    return jobrole


@router.get("/{jobrole_id}", response_model=schemas.JobRole)
def read_jobrole(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int
) -> Any:
    """
    Get jobrole by ID.
    """
    jobrole = crud.jobrole.get(db=db, id=jobrole_id)
    if not jobrole:
        raise HTTPException(status_code=404, detail="JobRole not found")
    return jobrole


@router.put("/{jobrole_id}", response_model=schemas.JobRole)
def update_jobrole(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int,
    jobrole_in: schemas.JobRoleUpdate
) -> Any:
    """
    Update a JobRole.
    """
    jobrole = crud.jobrole.get(db, id=jobrole_id)
    if not jobrole:
        raise HTTPException(
            status_code=404,
            detail="The jobrole with this jobrole_id does not exist in the system",
        )
    jobrole = crud.jobrole.update(db, db_obj=jobrole, obj_in=jobrole_in)
    return jobrole


@router.delete("/{jobrole_id}", response_model=List[schemas.JobRole])
def delete_jobrole(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int
) -> Any:
    """
    Delete a JobRole.
    """
    JobRole = crud.JobRole.get(db=db, id=jobrole_id,)
    if not JobRole:
        raise HTTPException(status_code=404, detail="JobRole not found")
    remaining_jobrole = crud.jobrole.remove(db=db, id=jobrole_id)
    return remaining_jobrole