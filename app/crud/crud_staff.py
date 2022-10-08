from app.crud.base import CRUDBase
from app.models.staff import Staff
from app.schemas.staff import StaffCreate, StaffUpdate

class CRUDStaff(CRUDBase[Staff, StaffCreate, StaffUpdate]):
    pass

staff = CRUDStaff(Staff)