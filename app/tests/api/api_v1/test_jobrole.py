from app.tests.utils.utils import random_num_in, random_num_out
from .test_base import LoadDataBase
from .test_skill import load_skill
from app import crud

load_jobrole = LoadDataBase("jobrole")


def test_read_jobroles(client) -> None:
    data = load_jobrole.base_data
    response = client.get(load_jobrole.base_url)
    skill = load_skill.base_data[0]
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