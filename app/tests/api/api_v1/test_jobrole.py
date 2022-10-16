from app.tests.utils.utils import random_num_in, random_num_out
from .test_base import LoadDataBase
from .test_skill import load_skill
from app import crud

load_jobrole = LoadDataBase("jobrole")


def test_read_jobroles(client) -> None:
    data = load_jobrole.base_data
    response = client.get(load_jobrole.base_url)
    skill = load_skill.base_data[5]
    assert response.status_code == 200
    for i in range(len(data)):
        for key, value in data[i].items():
            assert response.json()[i][key] == value
    assert skill in response.json()[0]["skills"]


def test_create_jobrole(client) -> None:
    data = load_jobrole.create_one_data
    response = client.post(load_jobrole.base_url, json=data)
    assert response.status_code == 200
    assert response.json()["jobrole_name"] == data["jobrole_name"]
    assert not response.json()["deleted"]


def test_create_jobrole_that_exists_alreaady(client) -> None:
    jobrole_name = load_jobrole.base_data[0]["jobrole_name"]
    response = client.post(load_jobrole.base_url, json={"jobrole_name": jobrole_name})
    assert response.status_code == 400


def test_read_jobrole(client) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    response = client.get(f"{load_jobrole.base_url}{id}")
    assert response.status_code == 200
    assert response.json() == data


def test_read_jobrole_that_does_not_exist(client) -> None:
    response = client.get(f"{load_jobrole.base_url}999")
    assert response.status_code == 404


def test_update_jobrole(client) -> None:
    update_data = load_jobrole.update_one_data
    data = load_jobrole.base_data[0]
    id = data["id"]
    response = client.put(f"{load_jobrole.base_url}{id}", json=update_data)
    update_data["id"] = id
    assert response.status_code == 200
    assert response.json()["jobrole_name"] == update_data["jobrole_name"]


def test_update_jobrole_that_does_not_exist(client) -> None:
    update_data = load_jobrole.update_one_data
    response = client.put(f"{load_jobrole.base_url}999", json=update_data)
    assert response.status_code == 404


def test_delete_jobrole(client) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    response = client.delete(f"{load_jobrole.base_url}{id}")
    assert response.status_code == 200
    assert response.json()["deleted"]


def test_delete_jobrole_that_does_not_exist(client) -> None:
    response = client.delete(f"{load_jobrole.base_url}999")
    assert response.status_code == 404


def test_delete_jobrole_that_is_already_deleted(client, session) -> None:
    crud.jobrole.remove(session, id=1)
    data = load_jobrole.base_data[0]
    id = data["id"]
    response = client.delete(f"{load_jobrole.base_url}{id}")
    assert response.status_code == 400

def test_add_skill_to_jobrole(client) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    skill = load_skill.base_data[0]
    response = client.post(f"{load_jobrole.base_url}{id}/new_skill/", params={"skill_id": skill["id"]})
    assert response.status_code == 200
    assert skill in response.json()["skills"]

def test_add_skill_to_jobrole_that_does_not_exist(client) -> None:
    skill = load_skill.base_data[0]
    response = client.post(f"{load_jobrole.base_url}999/new_skill/", params={"skill_id": skill["id"]})
    assert response.status_code == 404

def test_add_skill_to_jobrole_that_been_softdeleted(client, session) -> None:
    crud.jobrole.remove(session, id=1)
    skill = load_skill.base_data[0]
    response = client.post(f"{load_jobrole.base_url}1/new_skill/", params={"skill_id": skill["id"]})
    assert response.status_code == 400

def test_add_skill_to_jobrole_that_already_exists(client) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    skill = data["skills"][0]
    response = client.post(f"{load_jobrole.base_url}{id}/new_skill/", params={"skill_id": skill["id"]})
    assert response.status_code == 400

def test_add_softdeleted_skill_from_jobrole(client) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    skill = load_skill.base_data[3]
    response = client.post(f"{load_jobrole.base_url}{id}/new_skill/", params={"skill_id": skill["id"]})
    assert response.status_code == 400

def test_get_skills_for_jobrole(client) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    response = client.get(f"{load_jobrole.base_url}{id}/skills/")
    assert response.status_code == 200
    assert response.json() == data["skills"]

def test_get_skills_for_jobrole_that_does_not_exist(client) -> None:
    response = client.get(f"{load_jobrole.base_url}999/skills/")
    assert response.status_code == 404

def get_available_skills_for_jobrole(client) -> None:
    data = load_jobrole.base_data[0]
    response = client.get(f"{load_jobrole.base_url}/available_skills/")
    assert response.status_code == 200
    assert response.json() == data["skills"]

def test_get_available_jobroles(client) -> None:
    response = client.get(f"{load_jobrole.base_url}/available/")
    assert response.status_code == 200

def test_get_available_skills_for_jobrole(client) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    response = client.get(f"{load_jobrole.base_url}{id}/available_skills/")
    assert response.status_code == 200
    assert response.json() == data["skills"]

def test_get_available_skills_for_jobrole_that_does_not_exist(client) -> None:
    response = client.get(f"{load_jobrole.base_url}999/available_skills/")
    assert response.status_code == 404


def test_delete_skill_from_jobrole(client) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    skill = data["skills"][0]
    skill_id = skill["id"]
    response = client.delete(f"{load_jobrole.base_url}{id}/delete_skill/{skill_id}")
    assert response.status_code == 200
    for key, value in data.items():
        assert response.json()[key] == value
    assert skill not in response.json()["skills"]

def test_delete_skill_from_jobrole_that_does_not_exist(client) -> None:
    skill_id = load_skill.base_data[0]['id']
    response = client.delete(f"{load_jobrole.base_url}999/delete_skill/{skill_id}")
    assert response.status_code == 404

def test_delete_skill_that_does_not_exist_from_jobrole(client) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    response = client.delete(f"{load_jobrole.base_url}{id}/delete_skill/999")
    assert response.status_code == 404

