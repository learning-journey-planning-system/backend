from fastapi import APIRouter

from app.api.api_v1.endpoints import roles, staffs, skills, courses, jobroles,courseskill,jobroleskill

api_router = APIRouter()
api_router.include_router(staffs.router, prefix="/staffs", tags=["staffs"])
api_router.include_router(roles.router, prefix="/roles", tags=["roles"])
api_router.include_router(skills.router, prefix="/skills", tags=["skills"])
api_router.include_router(courses.router, prefix="/courses", tags=["courses"])
api_router.include_router(jobroles.router, prefix="/jobroles", tags=["jobroles"])
api_router.include_router(jobroleskill.router, prefix="/jobroleskills", tags=["jobroleskills"])
api_router.include_router(courseskill.router, prefix="/courseskills", tags=["courseskills"])