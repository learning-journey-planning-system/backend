from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Course])
def read_courses(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve courses.
    For SC24 View list of courses by admin.
    """
    courses = crud.course.get_multi(db)
    return courses


@router.post("/", response_model=schemas.Course)
def create_course(
    *,
    db: Session = Depends(deps.get_db),
    course_in: schemas.CourseCreate
) -> Any:
    """
    Create new course.
    """
    course = crud.course.get(db, id=course_in.id)
    if course:
        raise HTTPException(
            status_code=400,
            detail="The course with this course id already exists in the system.",
        )
    course = crud.course.create(db, obj_in=course_in)
    return course


@router.get("/{course_id}", response_model=schemas.CourseWithSkills)
def read_course(
    *,
    db: Session = Depends(deps.get_db),
    course_id: str
) -> Any:
    """
    Get course by ID.
    For SC22 view a course page.
    """
    course = crud.course.get(db=db, id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.put("/{course_id}", response_model=schemas.Course)
def update_course(
    *,
    db: Session = Depends(deps.get_db),
    course_id: str,
    course_in: schemas.CourseUpdate
) -> Any:
    """
    Update a course.
    """
    course = crud.course.get(db, id=course_id)
    if not course:
        raise HTTPException(
            status_code=404,
            detail="The course with this course id does not exist in the system",
        )
    course = crud.course.update(db, db_obj=course, obj_in=course_in)
    return course


@router.delete("/{course_id}", response_model=List[schemas.Course])
def delete_course(
    *,
    db: Session = Depends(deps.get_db),
    course_id: str
) -> Any:
    """
    Delete a course.
    """
    course = crud.course.get(db=db, id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    remaining_course = crud.course.remove(db=db, id=course_id)
    return remaining_course

@router.put("/{course_id}/new_skill/", response_model=schemas.CourseWithSkills)
def add_skill_to_course(
    *,
    db: Session = Depends(deps.get_db),
    course_id: str,
    skill_id: str
) -> Any:
    """
    Add a skill to a course.
    For SC19 assign skill to a course.

    If course is inactive or if skill has been soft deleted, 404 will be returned.
    """

    # Check if course exists
    course = crud.course.get(db, id=course_id)
    if not course:
        raise HTTPException(
            status_code=404,
            detail="The course with this course id does not exist in the system",
        )

    # Check if course is active
    if course.course_status == "Retired":
        raise HTTPException(
            status_code=404,
            detail="The course with this course id is not active.",
        )
    
    # Check if skill exists
    skill = crud.skill.get(db, id=skill_id)
    if not skill:
        raise HTTPException(
            status_code=404,
            detail="The skill with this skill id does not exist in the system",
        )
    
    # Check if skill has been soft deleted
    if skill.deleted:
        raise HTTPException(
            status_code=404,
            detail="The skill with this skill id has been soft deleted.",
        )
    
    # Check if skill is already in course
    if skill in course.skills:
        raise HTTPException(
            status_code=400,
            detail="The skill with this skill id is already in the course",
        )
    
    # Add skill to course
    course.skills.append(skill)
    db.commit()
    db.refresh(course)

    return course

@router.delete("/{course_id}/delete_skill/{skill_id}", response_model=schemas.CourseWithSkills)
def delete_skill_from_course(
    *,
    db: Session = Depends(deps.get_db),
    course_id: str,
    skill_id: str
) -> Any:
    """
    Delete a skill from a course.
    """

    # Check if course exists
    course = crud.course.get(db, id=course_id)
    if not course:
        raise HTTPException(
            status_code=404,
            detail="The course with this course id does not exist in the system",
        )
    
    # Check if skill exists
    skill = crud.skill.get(db, id=skill_id)
    if not skill:
        raise HTTPException(
            status_code=404,
            detail="The skill with this skill id does not exist in the system",
        )
    
    # Check if skill is in course
    if skill not in course.skills:
        raise HTTPException(
            status_code=400,
            detail="The skill with this skill id is not in the course",
        )
    
    # Delete skill from course
    course.skills.remove(skill)
    db.commit()
    db.refresh(course)

    return course