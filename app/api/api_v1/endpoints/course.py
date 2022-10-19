from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
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


@router.post("/{course_id}/new_skills/", response_model=List[List[str]])
def add_skills_to_course(
    *,
    db: Session = Depends(deps.get_db),
    course_id: str,
    skill_ids: List[int]
) -> Any:
    """
    Add skill(s) to a course.
    For SC19 assign skill to a course.

    If course does not exist or is not active, 404 will be returned.

    Otherwise, it will return a list of two lists of skills that were not added in this format:\n
    [  [ skills that are soft deleted ], [ skills that are already assigned to the course ]  ]

    If an empty list is returned, all skills were added successfully!
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
    
    soft_deleted = []
    already_assigned = []
    for skill_id in skill_ids:
        skill = crud.skill.get(db, id=skill_id)

        # Check if skill has been soft deleted
        if skill.deleted:
            soft_deleted.append(skill.skill_name)

        # Check if skill is already in course
        elif skill in course.skills:
            already_assigned.append(skill.skill_name)
        
        # Add skill to course
        else:
            course.skills.append(skill)
            db.commit()

    db.refresh(course)
    
    return [soft_deleted, already_assigned]


@router.delete("/{course_id}/delete_skill/{skill_id}", response_model=schemas.CourseWithSkills)
def delete_skill_from_course(
    *,
    db: Session = Depends(deps.get_db),
    course_id: str,
    skill_id: int
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


@router.get("/{course_id}/all_skills/", response_model=List[schemas.Skill])
def get_skills_for_course(
    *,
    db: Session = Depends(deps.get_db),
    course_id: str
) -> Any:
    """
    Get All Skills for a Course.
    For SC26 View skills of a course by admin. This is for admin panel

    Returns 404 if course not in database. 
    
    Returns list of skills for courses are <u>active</u>.
    For courses in retired/pending status, returns empty list.
    """

    # check if course exists in db
    course = crud.course.get(db=db, id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail="This course does not exist in the system")

    # get skills for course that are active
    if course.course_status == "Active":
        return course.skills
    return []

@router.get("/with_skills/", response_model=List[schemas.CourseWithSkills])
def read_courses_with_skills(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve all courses with their respective skills.
    """
    courses = crud.course.get_multi(db)
    return courses
