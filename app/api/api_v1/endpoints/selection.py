from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Selection])
def read_selections(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve selections.
    """
    selections = crud.selection.get_multi(db)
    return selections


@router.post("/", response_model=schemas.Selection)
def create_selection(
    *,
    db: Session = Depends(deps.get_db),
    selection_in: schemas.SelectionCreate
) -> Any:
    """
    Create new selection.
    """
    selection = crud.selection.get(db, obj_in=selection_in)
    if selection:
        raise HTTPException(
            status_code=400,
            detail="This selection already exists in the system.",
        )
    
    selection = crud.selection.create(db=db, obj_in=selection_in)
    return selection


@router.get("/lj_id={learningjourney_id}&c_id={course_id}", response_model=schemas.Selection)
def read_selection(
    *,
    db: Session = Depends(deps.get_db),
    learningjourney_id: int,
    course_id: str
) -> Any:
    """
    Get selection by learningjourney_id and course_id.
    """
    selection = crud.selection.get(db=db, learningjourney_id=learningjourney_id, course_id=course_id)
    if not selection:
        raise HTTPException(status_code=404, detail="Selection not found")
    return selection


# @router.put("/{selection_id}", response_model=schemas.Selection)
# def update_selection(
#     *,
#     db: Session = Depends(deps.get_db),
#     selection_id: int,
#     selection_in: schemas.SelectionUpdate
# ) -> Any:
#     """
#     Update an selection.
#     """
#     selection = crud.selection.get(db=db, id=selection_id)
#     if not selection:
#         raise HTTPException(status_code=404, detail="Selection not found")
#     selection = crud.selection.update(db=db, db_obj=selection, obj_in=selection_in)
#     return selection


@router.delete("/lj_id={learningjourney_id}&c_id={course_id}", response_model=List[schemas.Selection])
def delete_selection(
    *,
    db: Session = Depends(deps.get_db),
    learningjourney_id: int,
    course_id: str
) -> Any:
    """
    Delete a selection.
    """
    selection = crud.selection.get(db=db, learningjourney_id=learningjourney_id, course_id=course_id)
    if not selection:
        raise HTTPException(status_code=404, detail="Selection not found")
    remaining_selections = crud.selection.remove(db=db, learningjourney_id=learningjourney_id, course_id=course_id)
    return remaining_selections
