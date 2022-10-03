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
    jobrole_in: schemas.StaffUpdate
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
    remaining_staffs = crud.staff.remove(db=db, id=staff_id)
    return remaining_staffs