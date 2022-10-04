from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Skill])
def read_skills(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve skills.
    """
    skills = crud.skill.get_multi(db)
    return skills


@router.post("/", response_model=schemas.Skill)
def create_skills(
    *,
    db: Session = Depends(deps.get_db),
    skill_in: schemas.SkillCreate
) -> Any:
    """
    Create new Skill.
    """
    skill = crud.skill.get(db, id=skill_in.id)
    if skill:
        raise HTTPException(
            status_code=400,
            detail="The skill with this skill id already exists in the system.",
        )
    skill = crud.skill.create(db, obj_in=skill_in)
    return skill


@router.get("/{skill_id}", response_model=schemas.Skill)
def read_skill(
    *,
    db: Session = Depends(deps.get_db),
    skill_id: int
) -> Any:
    """
    Get skill by ID.
    """
    skill = crud.skill.get(db=db, id=skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail="skill not found")
    return skill


@router.put("/{skill_id}", response_model=schemas.Skill)
def update_skill(
    *,
    db: Session = Depends(deps.get_db),
    skill_id: int,
    skill_in: schemas.JobroleUpdate
) -> Any:
    """
    Update a skill.
    """
    skill = crud.skill.get(db, id=skill_id)
    if not skill:
        raise HTTPException(
            status_code=404,
            detail="The skill with this skill_id does not exist in the system",
        )
    skill = crud.skill.update(db, db_obj=skill, obj_in=skill_in)
    return skill


@router.delete("/{skill_id}", response_model=List[schemas.Skill])
def delete_skill(
    *,
    db: Session = Depends(deps.get_db),
    skill_id: int
) -> Any:
    """
    Delete a skill.
    """
    skill = crud.skill.get(db=db, id=skill_id,)
    if not skill:
        raise HTTPException(status_code=404, detail="skill not found")
    softdelete_skill = crud.skill.update(db=db, id=skill_id, deleted=True) # soft delete-need to test first
    return softdelete_skill