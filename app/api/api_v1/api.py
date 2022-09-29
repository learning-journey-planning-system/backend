from fastapi import APIRouter

from app.api.api_v1.endpoints import roles, staffs

api_router = APIRouter()
api_router.include_router(staffs.router, prefix="/users", tags=["users"])
api_router.include_router(roles.router, prefix="/items", tags=["items"])
