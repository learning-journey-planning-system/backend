from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Registration])
def read_registrations(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve registrations.
    """
    registrations = crud.registration.get_multi(db)
    return registrations


@router.post("/", response_model=schemas.Registration)
def create_registration(
    *,
    db: Session = Depends(deps.get_db),
    registration_in: schemas.RegistrationCreate
) -> Any:
    """
    Create new registration.
    """
    registration = crud.registration.get(db, id=registration_in.id, )
    if registration:
        raise HTTPException(
            status_code=400,
            detail="The registration with this registration id already exists in the system.",
        )
    registration = crud.registration.create(db=db, obj_in=registration_in)
    return registration


@router.get("/{registration_id}", response_model=schemas.Registration)
def read_registration(
    *,
    db: Session = Depends(deps.get_db),
    registration_id: int
) -> Any:
    """
    Get registration by ID.
    """
    registration = crud.registration.get(db=db, id=registration_id)
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    return registration


@router.put("/{registration_id}", response_model=schemas.Registration)
def update_registration(
    *,
    db: Session = Depends(deps.get_db),
    registration_id: int,
    registration_in: schemas.RegistrationUpdate
) -> Any:
    """
    Update a registration.
    """
    registration = crud.registration.get(db=db, id=registration_id)
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    registration = crud.registration.update(db=db, db_obj=registration, obj_in=registration_in)
    return registration


@router.delete("/{registration_id}", response_model=List[schemas.Registration])
def delete_registration(
    *,
    db: Session = Depends(deps.get_db),
    registration_id: int
) -> Any:
    """
    Delete a registration.
    """
    registration = crud.registration.get(db=db, id=registration_id)
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    remaining_registrations = crud.registration.remove(db=db, id=registration_id)
    return remaining_registrations
