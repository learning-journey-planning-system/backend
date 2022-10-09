from ast import Str
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
    SC13 View list of skills by admin.
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
    Checks if an existing skill with the same name exists already ('skill' and 'Skill' are considered the same name). If not then create a new skill with the specified name.
    """
    skill = crud.skill.get_by_skill_name(db, skill_name=skill_in.skill_name)
    if skill:
        raise HTTPException(
            status_code=400,
            detail="The skill with this skill name already exists in the system.",
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
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill


@router.put("/{skill_id}", response_model=schemas.Skill)
def update_skill(
    *,
    db: Session = Depends(deps.get_db),
    skill_id: int,
    skill_in: schemas.SkillUpdate
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


@router.delete("/{skill_id}", response_model=schemas.Skill)
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
        raise HTTPException(status_code=404, detail="Skill not found")
    if skill.deleted:
        raise HTTPException(status_code=400, detail="Skill has already been soft-deleted.")
    skill = crud.skill.remove(db=db, id=skill_id)
    return skill

@router.get("/{skill_id}/courses/", response_model=List[schemas.Course])
def get_courses_for_skill(
    *,
    db: Session = Depends(deps.get_db),
    skill_id: int
) -> Any:
    """
    Get All Courses for a Skill.
    For SC5 View all courses for a skill.

    Returns 404 if skill not in database or if skill has been soft deleted. 
    
    Only returns courses that are <u>active</u>.
    """

    # check if skill exists
    skill = crud.skill.get(db=db, id=skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    # check if skill has not been soft deleted
    if skill.deleted:
        raise HTTPException(status_code=404, detail="Skill has been soft deleted.")

    # filter out courses that are inactive
    courses = [course for course in skill.courses if course.course_status == "Active"]

    return courses

@router.get("/available/", response_model=List[schemas.Skill])
def get_available_skills(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve skills that are not soft deleted.
    SC27 Get all available skills that are not soft deleted.
    """
    skills = crud.skill.get_multi(db)
    available_skills = [skill for skill in skills if not skill.deleted]
    return available_skills