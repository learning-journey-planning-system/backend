from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.schemas.staff import StaffCreate
from app.schemas.role import RoleCreate
from app.tests.utils.utils import random_email, random_lower_string

# test data
staff_in = StaffCreate(
        id = 1,
        staff_fname = "Cheryl",
        staff_lname = "Goh",
        dept = "IT",
        email= "cherylgohsp@gmail.com",
        role_id = "1",
        password = "password"
    )

# happy path
def test_read_staffs(
    client: TestClient
) -> None:
    r = client.get(f"{settings.API_V1_STR}/staffs/me")
    current_staff = r.json()
    assert current_staff
    assert current_staff["is_active"] is True
    assert current_staff["is_superstaff"]
    assert current_staff["email"] == settings.FIRST_SUPERUSER

# happy path
def test_get_staff(
    client: TestClient, db: Session
) -> None:

    role_in = RoleCreate(
        id = 1,
        role_name = "Developer")
    role = crud.role.create(db, obj_in=role_in)

    staff = crud.staff.create(db, obj_in=staff_in)
    staff_id = staff.id
    r = client.get(
        f"{settings.API_V1_STR}/staffs/{staff_id}"
    )

    assert 200 <= r.status_code < 300
    api_staff = r.json()
    existing_staff = crud.staff.get(db=db, id=staff_id)
    assert existing_staff
    assert existing_staff.email == api_staff["email"]
    assert existing_staff.id == api_staff["id"]
    assert existing_staff.staff_fname == api_staff["staff_fname"]
    assert existing_staff.staff_lname == api_staff["staff_lname"]
    assert existing_staff.dept == api_staff["dept"]
    assert existing_staff.email== api_staff["email"]
    assert existing_staff.role_id == api_staff["role_id"]


# negative path
def test_create_staff_existing_id(
    client: TestClient, db: Session
) -> None:
    crud.staff.create(db, obj_in=staff_in)
    data = {"id": staff_in.id, 
            "password": staff_in.password}
    r = client.post(
        f"{settings.API_V1_STR}/staffs/", json=data,
    )
    created_staff = r.json()
    assert r.status_code == 400
    assert "id" not in created_staff