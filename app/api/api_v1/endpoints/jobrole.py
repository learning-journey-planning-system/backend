from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Jobrole])
def read_jobroles(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve Jobroles.
    """
    jobroles = crud.jobrole.get_multi(db)
    return jobroles


@router.post("/", response_model=schemas.Jobrole)
def create_jobrole(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_in: schemas.JobroleCreate
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


@router.get("/{jobrole_id}", response_model=schemas.Jobrole)
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
        raise HTTPException(status_code=404, detail="Jobrole not found")
    return jobrole


@router.put("/{jobrole_id}", response_model=schemas.Jobrole)
def update_jobrole(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int,
    jobrole_in: schemas.JobroleUpdate
) -> Any:
    """
    Update a Jobrole.
    """
    jobrole = crud.jobrole.get(db, id=jobrole_id)
    if not jobrole:
        raise HTTPException(
            status_code=404,
            detail="The jobrole with this jobrole_id does not exist in the system",
        )
    jobrole = crud.jobrole.update(db, db_obj=jobrole, obj_in=jobrole_in)
    return jobrole


@router.delete("/{jobrole_id}", response_model=List[schemas.Jobrole])
def delete_jobrole(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int
) -> Any:
    """
    Delete a Jobrole.
    """
    Jobrole = crud.Jobrole.get(db=db, id=jobrole_id,)
    if not Jobrole:
        raise HTTPException(status_code=404, detail="Jobrole not found")
    softdelete_jobrole = crud.jobrole.update(db=db, id=jobrole_id, deleted=True) # soft delete-need to test first
    return softdelete_jobrole