from typing import Generic, TypeVar
from sqlalchemy.orm import Session
from app.db.base_class import Base
import json
from app.db.base_class import Base
from app.crud.base import CRUDBase
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Base)
CRUDType = TypeVar("CRUDType", bound=CRUDBase)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)

from app import crud, models, schemas

class BaseJsonSeeder(Generic[ModelType, CRUDType, CreateSchemaType]):
    def __init__(self, model: ModelType, crud: CRUDType, CreateSchema: CreateSchemaType):
        self.model = model
        self.crud = crud
        self.CreateSchema = CreateSchema
    
    def json_seed(self, db):
        try:
            data = json.load(open("app/tests/db/test_data/%s/base.json" % self.model.__name__.lower()))
            for entry_data in data:
                new_entry = self.CreateSchema(**entry_data)
                self.crud.create(db, obj_in=new_entry)
            print(f"✅ {self.model.__name__} data created.")
        except FileNotFoundError:
            print(f"⛔️ {self.model.__name__} has no test data provided.")

course_json_seeder = BaseJsonSeeder(models.Course, crud.course, schemas.CourseCreate)
jobrole_json_seeder = BaseJsonSeeder(models.JobRole, crud.jobrole, schemas.JobRoleCreate)
learningjourney_json_seeder = BaseJsonSeeder(models.LearningJourney, crud.learningjourney, schemas.LearningJourneyCreate)
registration_json_seeder = BaseJsonSeeder(models.Registration, crud.registration, schemas.RegistrationCreate)
role_json_seeder = BaseJsonSeeder(models.Role, crud.role, schemas.RoleCreate)
skill_json_seeder = BaseJsonSeeder(models.Skill, crud.skill, schemas.SkillCreate)
staff_json_seeder = BaseJsonSeeder(models.Staff, crud.staff, schemas.StaffCreate)


def seed_all_test_data(db: Session) -> None:
    print("\n\nSeeding test data... 🥸\n")
    course_json_seeder.json_seed(db)
    jobrole_json_seeder.json_seed(db)
    learningjourney_json_seeder.json_seed(db)
    registration_json_seeder.json_seed(db)
    role_json_seeder.json_seed(db)
    skill_json_seeder.json_seed(db)
    staff_json_seeder.json_seed(db)