from fastapi import APIRouter

from app.api.api_v1.endpoints import roles, staffs

api_router = APIRouter()
api_router.include_router(staffs.router, prefix="/staffs", tags=["staff"])
api_router.include_router(roles.router, prefix="/roles", tags=["role"])
