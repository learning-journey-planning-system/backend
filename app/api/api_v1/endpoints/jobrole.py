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
    Checks if an existing jobrole with the same name exists already ('jobrole' and 'Jobrole' are considered the same name). If not then create a new jobrole with the specified name.
    """
    # check if jobrole with same name exists
    jobrole = crud.jobrole.get_by_jobrole_name(db, jobrole_name=jobrole_in.jobrole_name)
    if jobrole:
        raise HTTPException(
            status_code=400,
            detail="The jobrole with this jobrole name already exists in the system.",
        )
    jobrole = crud.jobrole.create(db, obj_in=jobrole_in)
    return jobrole


@router.get("/{jobrole_id}", response_model=schemas.JobRoleWithSkillsWithCourses)
def read_jobrole(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int
) -> Any:
    """
    Get full details of jobrole by ID.
    For SC7.
    Returns jobrole details, skills needed for jobrole and the courses related to the skills.
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
    SC16 Update JobRole in LJPS
    """
    jobrole = crud.jobrole.get(db, id=jobrole_id)
    if not jobrole:
        raise HTTPException(
            status_code=404,
            detail="The JobRole with this jobrole_id does not exist in the system",
        )
    if jobrole.deleted:
        raise HTTPException(
            status_code=400,
            detail="The JobRole with this jobrole_id has been deleted",
        )
    jobrole_name = jobrole.jobrole_name
    if jobrole_name == jobrole_in.jobrole_name:
        raise HTTPException(
            status_code=404,
            detail="The JobRole name is the same as the current JobRole name",
        )
    jobroles = crud.jobrole.get_multi(db)
    jobroles_names = [jobrole.jobrole_name for jobrole in jobroles]
    if jobrole_in.jobrole_name in jobroles_names:
        raise HTTPException(
            status_code=404,
            detail="The JobRole name already exists in the system",
        )

    jobrole = crud.jobrole.update(db, db_obj=jobrole, obj_in=jobrole_in)
    return jobrole

    

@router.delete("/{jobrole_id}", response_model=schemas.JobRole)
def delete_jobrole(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int
) -> Any:
    """
    Delete a JobRole.
    For SC17 Deleting job roles from LJPS.
    """
    jobrole = crud.jobrole.get(db=db, id=jobrole_id,)
    if not jobrole:
        raise HTTPException(status_code=404, detail="JobRole not found")
    if jobrole.deleted:
        raise HTTPException(
            status_code=400,
            detail="The jobrole with this jobrole_id has already been deleted",
        )
    jobrole = crud.jobrole.remove(db=db, id=jobrole_id)
    return jobrole

@router.post("/{jobrole_id}/new_skills/", response_model=List[List[str]])
def add_skills_to_jobrole(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int,
    skill_ids: List[int]
) -> Any:
    """
    Add skill(s) to a JobRole.
    For SC18 Assign skill to jobrole.

    If jobrole does not exist or is soft deleted, 404 will be returned.

    Otherwise, it will return a list of two lists of skills that were not added in this format:\n
    [  [ skills that are soft deleted ], [ skills that are already assigned to the course ]  ]

    If an empty list is returned, all skills were added successfully!
    """

    # Check if jobrole exists
    jobrole = crud.jobrole.get(db, id=jobrole_id)
    if not jobrole:
        raise HTTPException(
            status_code=404,
            detail="The jobrole with this jobrole id does not exist in the system",
        )

    # Check if jobrole is not soft deleted
    if jobrole.deleted:
        raise HTTPException(
            status_code=404,
            detail="The jobrole with this jobrole id has been soft deleted.",
        )
    
    soft_deleted = []
    already_assigned = []
    for skill_id in skill_ids:
        skill = crud.skill.get(db, id=skill_id)

        # Check if skill has been soft deleted
        if skill.deleted:
            soft_deleted.append(skill.skill_name)

        # Check if skill is already in jobrole
        elif skill in jobrole.skills:
            already_assigned.append(skill.skill_name)
        
        # Add skill to course
        else:
            jobrole.skills.append(skill)
            db.commit()

    db.refresh(jobrole)
    
    return [soft_deleted, already_assigned]


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

@router.delete("/{jobrole_id}/delete_skill/{skill_id}", response_model=schemas.JobRoleWithSkills)
def delete_skill_from_jobrole(
    *,
    db: Session = Depends(deps.get_db),
    jobrole_id: int,
    skill_id: int
) -> Any:
    """
    Delete a skill from a jobrole.
    SC12 Delete skill from job role API. This is for admin, and will be used in admin panel.
    """

    # Check if the jobrole exists
    jobrole = crud.jobrole.get(db, id=jobrole_id)
    if not jobrole:
        raise HTTPException(status_code=404,detail="The jobrole with this jobrole_id does not exist in the system")

    # Check if the jobrole has not been soft deleted
    if jobrole.deleted:
        raise HTTPException(status_code=404,detail="The jobrole with this jobrole_id has been soft deleted")

    # Check if the skill exists
    skill = crud.skill.get(db=db, id=skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    
    # Check if the skill has not been soft deleted
    if skill.deleted:
        raise HTTPException(status_code=404, detail="Skill with this skill_id has been soft deleted")
    
    # Check if the skill exist in the jobrole
    if skill not in jobrole.skills:
        raise HTTPException(status_code=400,detail="Jobrole has no such skill.")
    
    # Remove the skill from the jobrole
    jobrole.skills.remove(skill)
    db.commit()
    db.refresh(jobrole)

    return jobrole