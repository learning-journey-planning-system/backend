from .test_base import load_skill, load_course
from app import crud


def test_read_skills(client) -> None:
    data = load_skill.base_data
    response = client.get(load_skill.base_url)
    assert response.status_code == 200
    assert response.json() == data

def test_create_skill(client) -> None:
    data = load_skill.create_one_data
    response = client.post(load_skill.base_url, json=data)
    assert response.status_code == 200
    assert response.json()['skill_name'] == data['skill_name']

def test_create_skill_that_exists(client) -> None:
    data = load_skill.base_data[0]
    client.post(load_skill.base_url, json=data)
    response = client.post(load_skill.base_url, json=data)
    assert response.status_code == 400

def test_read_skill(client) -> None:
    data = load_skill.base_data[0]
    id = data["id"]
    response = client.get(f"{load_skill.base_url}{id}")
    assert response.status_code == 200
    assert response.json() == data

def test_read_skill_that_does_not_exist(client) -> None:
    response = client.get(f"{load_skill.base_url}999")
    assert response.status_code == 404

def test_update_skill(client) -> None:
    update_data = load_skill.update_one_data
    data = load_skill.base_data[0]
    id = data["id"]
    response = client.put(f"{load_skill.base_url}{id}", json=update_data)
    update_data["id"] = id
    assert response.status_code == 200
    for key, value in update_data.items():
        assert response.json()[key] == value
    assert response.json()["id"] == id

def test_update_skill_that_does_not_exist(client) -> None:
    update_data = load_skill.update_one_data
    response = client.put(f"{load_skill.base_url}999", json=update_data)
    assert response.status_code == 404

def test_delete_skill(client) -> None:
    data = load_skill.base_data[0]
    id = data["id"]
    response = client.delete(f"{load_skill.base_url}{id}")
    assert response.status_code == 200
    assert response.json()["deleted"]

def test_delete_skill_that_does_not_exist(client) -> None:
    response = client.delete(f"{load_skill.base_url}999")
    assert response.status_code == 404

def test_delete_skill_that_has_been_deleted(client,session) -> None:
    crud.skill.remove(session, id=1)
    data = load_skill.base_data[0]
    id = data["id"]
    response = client.delete(f"{load_skill.base_url}{id}")
    assert response.status_code == 400

def test_get_courses_for_skill(client) -> None:
    data = load_skill.base_data[0]
    id = data["id"]
    course = load_course.base_data[0]
    response = client.get(f"{load_skill.base_url}{id}/courses/")
    assert response.status_code == 200
    assert response.json() == [course]

def test_get_courses_for_skill_that_does_not_exist(client) -> None:
    response = client.get(f"{load_skill.base_url}999/courses/")
    assert response.status_code == 404

def test_get_courses_for_skill_that_has_been_deleted(client,session) -> None:
    crud.skill.remove(session, id=1)
    data = load_skill.base_data[0]
    id = data["id"]
    response = client.get(f"{load_skill.base_url}{id}/courses/")
    assert response.status_code == 404

def test_get_courses_for_skill_that_has_no_courses(client) -> None:
    data = load_skill.base_data[1]
    id = data["id"]
    response = client.get(f"{load_skill.base_url}{id}/courses/")
    assert response.status_code == 200
    assert response.json() == []

def test_get_available_skills(client, session) -> None:

    # delete one jobrole record
    delete_id = load_skill.base_data[0]["id"]
    delete_skill = load_skill.base_data[0]
    crud.skill.remove(session, id=delete_id)

    # load the rest of the records
    data = load_skill.base_data[1:]
    response = client.get(f"{load_skill.base_url}available/")

    # check the response
    assert response.status_code == 200

    # check if soft deleted record is not in the response
    inside = False
    for record in response.json():
        if record["id"] == delete_id:
            inside = True
    assert not inside

