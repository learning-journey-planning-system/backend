from typing import Generic, Type, TypeVar
import csv

from app.db.base_class import Base
from app.crud.base import CRUDBase
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType", bound=Base)
CRUDType = TypeVar("CRUDType", bound=CRUDBase)

class SeederBase(Generic[ModelType, CRUDType]):
    def __init__(self, model: Type[ModelType], crud: Type[CRUDType]):
        self.model = model
        self.crud = crud

    def seed(self, db: Session) -> None:
        print('---- Seeding %s ----' % self.model.__name__)

        with open('app/db/RawData/%s.csv' % self.model.__name__.lower(), newline='') as f:
            data = csv.reader(f, delimiter=',')
            line = 0
            for row in data:
                if line == 0:
                    columns = row
                    print(f'Column names are {", ".join(row)}')
                    line += 1
                else:
                    mapping = {}
                    for i in range(1, len(columns)):
                        mapping[columns[i].lower()] = row[i]

                    db_obj = self.model(id = row[0], **mapping)
                    self.crud.create(db, obj_in=db_obj)
                    line += 1
            print(f'✅ Seeded {line} rows of data.\n')

from app.models import Course, Registration, Role, Staff
from app.crud import course, registration, role, staff

course = SeederBase(Course, course)
registration = SeederBase(Registration, registration)
role = SeederBase(Role, role)
staff = SeederBase(Staff, staff)