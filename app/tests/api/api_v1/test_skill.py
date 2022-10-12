from .test_base import LoadDataBase
from app import crud

load_skill = LoadDataBase("skill")


def test_read_skills(client) -> None:
    data = load_skill.base_data
    response = client.get(load_skill.base_url)
    assert response.status_code == 200
    assert response.json() == data


def test_create_skill(client) -> None:
    data = load_skill.create_one_data
    response = client.post(load_skill.base_url, json=data)
    assert response.status_code == 200
    assert response.json() == data


def test_read_skill(client) -> None:
    data = load_skill.base_data[0]
    id = data["id"]
    response = client.get(f"{load_skill.base_url}{id}")
    assert response.status_code == 200
    assert response.json() == data


def test_update_skill(client) -> None:
    update_data = load_skill.update_one_data
    data = load_skill.base_data[0]
    id = data["id"]
    response = client.put(f"{load_skill.base_url}{id}", json=update_data)
    update_data["id"] = id
    assert response.status_code == 200
    assert response.json() == update_data


def test_delete_skill(client) -> None:
    data = load_skill.base_data[0]
    id = data["id"]
    response = client.delete(f"{load_skill.base_url}{id}")
    assert response.status_code == 200
    assert data not in response.json()

#The skill with this skill name already exists in the system.
def test_create_skillname_that_exists(client) -> None:
    data = load_skill.create_one_data
    client.post(load_skill.base_url, json=data)
    response = client.post(load_skill.base_url, json=data)
    assert response.status_code == 400

#Skill not found
def test_read_skill_that_does_not_exist(client) -> None:
    response = client.get(f"{load_skill.base_url}999")
    assert response.status_code == 404

# The skill with this skill_id does not exist in the system for update
def test_update_skill_that_does_not_exist(client) -> None:
    update_data = load_skill.update_one_data
    response = client.put(f"{load_skill.base_url}999", json=update_data)
    assert response.status_code == 404

#Skill not found for soft deletion
def test_delete_skill_that_does_not_exist(client) -> None:
    response = client.delete(f"{load_skill.base_url}999")
    assert response.status_code == 404
