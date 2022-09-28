from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.role import create_random_role


def test_create_role(
    client: TestClient, db: Session
) -> None:
    data = {"id": "1", "role_name": "TestRole"}
    response = client.post(
        f"{settings.API_V1_STR}/roles/", json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == data["id"]
    assert content["role_name"] == data["role_name"]
    assert "id" in content
    assert "role_name" in content


def test_read_role(
    client: TestClient, db: Session
) -> None:
    role = create_random_role(db)
    response = client.get(
        f"{settings.API_V1_STR}/roles/{role.id}"
    )
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == role.id
    assert content["role_name"] == role.role_name