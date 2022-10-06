from app.crud.base import CRUDBase
from app.models.staff import Staff
from app.schemas.staff import StaffCreate, StaffUpdate

staff = CRUDBase[Staff, StaffCreate, StaffUpdate](Staff)