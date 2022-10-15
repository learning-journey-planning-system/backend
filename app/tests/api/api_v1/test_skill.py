from .test_course import load_course
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
    data = load_skill.base_data[0]
    id = data["id"]
    update_data = load_skill.update_one_data
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
def test_create_skill_that_exists(client) -> None:
    data = load_skill.base_data[0]
    response = client.post(load_skill.base_url, json=data)
    assert response.status_code == 400

#Skill not found
def test_read_skill_that_does_not_exist(client) -> None:
    response = client.get(f"{load_skill.base_url}999")
    assert response.status_code == 404

#The skill with this skill_id does not exist in the system for update
def test_update_skill_that_does_not_exist(client) -> None:
    update_data = load_skill.update_one_data
    response = client.put(f"{load_skill.base_url}999", json=update_data)
    assert response.status_code == 404

# Skill not found for delete
def test_delete_skill_that_does_not_exist(client) -> None:
    response = client.delete(f"{load_skill.base_url}999")
    assert response.status_code == 404

def test_get_courses_for_skill(client) -> None:
    data = load_skill.base_data[0]
    id = data["id"]
    course = load_course.base_data[0]
    response = client.get(f"{load_skill.base_url}{id}/courses/")
    assert response.status_code == 200
    assert course in response.json()

def test_get_courses_for_skill_that_does_not_exist(client) -> None:
    response = client.get(f"{load_skill.base_url}999/courses/")
    assert response.status_code == 404

def test_get_course_for_a_softdeleted_skill(client) -> None:
    data = load_skill.base_data[3]
    id = data["id"]
    response = client.get(f"{load_skill.base_url}{id}/courses/")
    assert response.status_code == 404

def test_get_courses_for_skill_that_has_no_courses(client) -> None:
    data = load_skill.base_data[4]
    id = data["id"]
    response = client.get(f"{load_skill.base_url}{id}/courses/")
    assert response.json() == []

def test_get_available_skills(client) -> None:
    response = client.get(f"{load_skill.base_url}/available/")
    assert response.status_code == 200
