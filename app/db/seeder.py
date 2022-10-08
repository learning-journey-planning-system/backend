from .seeder_base import SeederBase
from sqlalchemy.orm import Session

from app.models import Course, Registration, Role, Staff
from app.crud import CRUDCourse, CRUDRegistration, CRUDRole, CRUDStaff
from app.crud import course, registration, role, staff

class StaffSeeder(SeederBase[Staff, CRUDStaff]):

    # manually edit column name as it does not match out db naming conventions
    def edit_col_names(self, row):
        for i in range(len(row)):
            if row[i] == 'Role':
                row[i] = 'Role_ID'
        return row

course_seeder = SeederBase[Course, CRUDCourse](Course, course)
registration_seeder = SeederBase[Registration, CRUDRegistration](Registration, registration)
role_seeder = SeederBase[Role, CRUDRole](Role, role)
staff_seeder = StaffSeeder(Staff, staff)

def seed_all(db: Session) -> None:
    role_seeder.seed(db)
    staff_seeder.seed(db)
    course_seeder.seed(db)
    registration_seeder.seed(db)