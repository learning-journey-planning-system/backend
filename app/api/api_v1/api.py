from fastapi import APIRouter

from app.api.api_v1.endpoints import learningjourney, role, staff, skill, selection, course, registration, jobrole, courseskill, jobroleskill

api_router = APIRouter()
api_router.include_router(staff.router, prefix="/staff", tags=["staff"])
api_router.include_router(role.router, prefix="/role", tags=["role"])
api_router.include_router(skill.router, prefix="/skill", tags=["skill"])
api_router.include_router(course.router, prefix="/course", tags=["course"])
api_router.include_router(jobrole.router, prefix="/jobrole", tags=["jobrole"])
api_router.include_router(jobroleskill.router, prefix="/jobroleskill", tags=["jobroleskill"])
api_router.include_router(courseskill.router, prefix="/courseskill", tags=["courseskill"])
api_router.include_router(learningjourney.router, prefix="/learningjourney", tags=["learningjourney"])
api_router.include_router(registration.router, prefix="/registration", tags=["registration"])
api_router.include_router(selection.router, prefix="/selection", tags=["selection"])
