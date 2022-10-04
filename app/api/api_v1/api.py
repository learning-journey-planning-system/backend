from fastapi import APIRouter

from app.api.api_v1.endpoints import learningjourney, registration, roles, selection, staffs

api_router = APIRouter()
api_router.include_router(staffs.router, prefix="/staffs", tags=["staff"])
api_router.include_router(roles.router, prefix="/roles", tags=["role"])
api_router.include_router(learningjourney.router, prefix="/learningjourneys", tags=["learningjourney"])
api_router.include_router(registration.router, prefix="/registration", tags=["registration"])
api_router.include_router(selection.router, prefix="/selection", tags=["selection"])

