from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Role])
def read_roles(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve roles.
    """
    roles = crud.role.get_multi(db)
    return roles


@router.post("/", response_model=schemas.Role)
def create_role(
    *,
    db: Session = Depends(deps.get_db),
    role_in: schemas.RoleCreate
) -> Any:
    """
    Create new role.
    """
    role = crud.role.get(db, id=role_in.id)
    if role:
        raise HTTPException(
            status_code=400,
            detail="The role with this role id already exists in the system.",
        )
    role = crud.role.create(db=db, obj_in=role_in)
    return role


@router.get("/{role_id}", response_model=schemas.Role)
def read_role(
    *,
    db: Session = Depends(deps.get_db),
    role_id: int
) -> Any:
    """
    Get role by ID.
    """
    role = crud.role.get(db=db, id=role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.put("/{role_id}", response_model=schemas.Role)
def update_role(
    *,
    db: Session = Depends(deps.get_db),
    role_id: int,
    role_in: schemas.RoleUpdate
) -> Any:
    """
    Update an role.
    """
    role = crud.role.get(db=db, id=role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    role = crud.role.update(db=db, db_obj=role, obj_in=role_in)
    return role


@router.delete("/{role_id}", response_model=schemas.Role)
def delete_role(
    *,
    db: Session = Depends(deps.get_db),
    role_id: int
) -> Any:
    """
    Delete an role.
    """
    role = crud.role.get(db=db, id=role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    remaining_roles = crud.role.remove(db=db, id=role_id)
    return remaining_roles
