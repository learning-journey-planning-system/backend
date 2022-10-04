from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.JobRoleSkill])
def read_jobroleskills(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve JobRoleSkills.
    """
    jobroleskills = crud.jobroleskill.get_multi(db)
    return jobroleskills


@router.post("/", response_model=schemas.JobRoleSkill)
def create_jobroleskill(
    *,
    db: Session = Depends(deps.get_db),
    jobroleskill_in: schemas.JobRoleSkillCreate
) -> Any:
    """
    Create new jobroleskill.
    """
    jobroleskill = crud.jobroleskill.get(db, jobrole_id=jobroleskill_in.jobrole_id, skill_id=jobroleskill_in.skill_id)
    if jobroleskill:
        raise HTTPException(
            status_code=400,
            detail="The JobRoleSkill with this jobrole id and skill id already exists in the system.",
        )
    jobroleskill = crud.jobroleskill.create(db=db, obj_in=jobroleskill_in)
    return jobroleskill


@router.get("/{jobrole_id}/{skill_id}", response_model=schemas.JobRoleSkill)
def read_jobroleskill(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int,
    skill_id: str
) -> Any:
    """
    Get jobroleskill by jobrole_id and skill_id.
    """
    jobroleskill = crud.jobroleskill.get(db=db, jobrole_id=jobrole_id, skill_id=skill_id)
    if not jobroleskill:
        raise HTTPException(status_code=404, detail="JobRoleSkill not found")
    return jobroleskill


# @router.put("/{jobroleskill_id}", response_model=schemas.JobRoleSkill)
# def update_jobroleskill(
#     *,
#     db: Session = Depends(deps.get_db),
#     jobroleskill_id: int,
#     jobroleskill_in: schemas.JobRoleSkillUpdate
# ) -> Any:
#     """
#     Update an JobRoleSkill.
#     """
#     jobroleskill = crud.jobroleskill.get(db=db, id=jobroleskill_id)
#     if not jobroleskill:
#         raise HTTPException(status_code=404, detail="Skill not found")
#     jobroleskill = crud.jobroleskill.update(db=db, db_obj=jobroleskill, obj_in=jobroleskill_in)
#     return jobroleskill


@router.delete("/{jobrole_id}/{skill_id}", response_model=List[schemas.JobRoleSkill])
def delete_jobroleskill(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int,
    skill_id: str
) -> Any:
    """
    Delete an jobroleskill.
    """
    jobroleskill = crud.jobroleskill.get(db=db, jobrole_id=jobrole_id, skill_id=skill_id)
    if not jobroleskill:
        raise HTTPException(status_code=404, detail="JobRoleSkill not found")
    remaining_jobroleskill = crud.jobroleskill.remove(db=db, jobrole_id=jobrole_id, skill_id=skill_id)
    return remaining_jobroleskill
