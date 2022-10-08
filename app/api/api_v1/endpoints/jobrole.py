from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.JobRoleWithSkills])
def read_jobroles(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve JobRoles.
    For SC15 View list of job roles by admin (This is for admin panel)
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
    JobRole = crud.jobrole.get(db=db, id=jobrole_id,)
    if not JobRole:
        raise HTTPException(status_code=404, detail="JobRole not found")
    remaining_jobrole = crud.jobrole.remove(db=db, id=jobrole_id)
    return remaining_jobrole

@router.put("/{jobrole_id}/new_skill/", response_model=schemas.JobRoleWithSkills)
def add_skill_to_jobrole(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int,
    skill_id: str
) -> Any:
    """
    Add a skill to a JobRole.
    For SC18 Assign skill to jobrole.

    If jobrole or skill has been soft deleted or does not exists, 404 will be returned.
    """

    # Check if jobrole exists
    jobrole = crud.jobrole.get(db, id=jobrole_id)
    if not jobrole:
        raise HTTPException(
            status_code=404,
            detail="The jobrole with this jobrole_id does not exist in the system",
        )
    
    # Check if jobrole has not been soft deleted
    if jobrole.deleted:
        raise HTTPException(
            status_code=404,
            detail="The jobrole with this jobrole_id has been soft deleted",
        )
    
    # Check if skill exists
    skill = crud.skill.get(db, id=skill_id)
    if not skill:
        raise HTTPException(
            status_code=404,
            detail="The skill with this skill_id does not exist in the system",
        )
    
    # Check if skill has not been soft deleted
    if skill.deleted:
        raise HTTPException(
            status_code=404,
            detail="The skill with this skill_id has been soft deleted",
        )
    
    # Check if skill is already assigned to jobrole
    if skill in jobrole.skills:
        raise HTTPException(
            status_code=400,
            detail="The skill with this skill_id is already assigned to this jobrole",
        )
    
    # Add skill to jobrole
    jobrole.skills.append(skill)
    db.commit()
    db.refresh(jobrole)
    return jobrole

@router.get("/{jobrole_id}/skills/", response_model=List[schemas.Skill])
def get_skills_for_jobrole(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int
) -> Any:
    """
    Get skills for each role.
    SC25 This is for admin panel
    """

    # Check if jobrole exists
    jobrole = crud.jobrole.get(db, id=jobrole_id)
    if not jobrole:
        raise HTTPException(
            status_code=404,
            detail="The jobrole with this jobrole_id does not exist in the system",
        )
    
    return jobrole.skills

@router.get("/available/", response_model=List[schemas.JobRoleWithSkills])
def get_available_jobroles(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve JobRoles that are available. Meaning deleted = 0.
    For SC1 View available job roles by learner.
    Note: For each jobrole, only the skills that are available are also returned.
    """
    jobroles = crud.jobrole.get_multi_available(db)

    # Filter out skills that are deleted
    for jobrole in jobroles:
        jobrole.skills = [skill for skill in jobrole.skills if skill.deleted == 0]

    return jobroles

@router.get("/{jobrole_id}/available_skills/", response_model=List[schemas.Skill])
def get_available_skills_for_jobrole(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int
) -> Any:
    """
    Get skills for each role.
    SC3 View available skills for a jobrole. This is for learner.
    """

    # Check if jobrole exists
    jobrole = crud.jobrole.get(db, id=jobrole_id)
    if not jobrole:
        raise HTTPException(
            status_code=404,
            detail="The jobrole with this jobrole_id does not exist in the system",
        )
    
    # Filter out deleted skills
    available_skills = [skill for skill in jobrole.skills if skill.deleted == 0]
    
    return available_skills