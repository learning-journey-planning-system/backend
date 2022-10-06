from fastapi import APIRouter

from app.api.endpoints import learningjourney, role, staff, skill, course, registration, jobrole

api_router = APIRouter()
api_router.include_router(course.router, prefix="/course", tags=["course"])
api_router.include_router(jobrole.router, prefix="/jobrole", tags=["jobrole"])
api_router.include_router(learningjourney.router, prefix="/learningjourney", tags=["learningjourney"])
api_router.include_router(registration.router, prefix="/registration", tags=["registration"])
api_router.include_router(role.router, prefix="/role", tags=["role"])
api_router.include_router(skill.router, prefix="/skill", tags=["skill"])
api_router.include_router(staff.router, prefix="/staff", tags=["staff"])