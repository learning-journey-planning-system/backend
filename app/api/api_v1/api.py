from fastapi import APIRouter

from app.api.api_v1.endpoints import learningjourney, role, staff, skill, course, registration, jobrole

api_router = APIRouter()
api_router.include_router(course.router, prefix="/course", tags=["Course"])
api_router.include_router(jobrole.router, prefix="/jobrole", tags=["Job Role"])
api_router.include_router(learningjourney.router, prefix="/learningjourney", tags=["Learning Journey"])
api_router.include_router(registration.router, prefix="/registration", tags=["Registration"])
api_router.include_router(role.router, prefix="/role", tags=["Role"])
api_router.include_router(skill.router, prefix="/skill", tags=["Skill"])
api_router.include_router(staff.router, prefix="/staff", tags=["Staff"])