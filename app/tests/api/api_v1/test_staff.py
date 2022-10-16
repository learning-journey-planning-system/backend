from .test_base import load_staff,load_learningjourney
from app import crud

def test_read_staffs(client) -> None:
    data = load_staff.base_data
    response = client.get(load_staff.base_url)
    assert response.status_code == 200
    assert response.json() == data

def test_create_staff(client) -> None:
    data = load_staff.create_one_data
    response = client.post(load_staff.base_url, json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_create_staff_that_exists(client) -> None:
    data = load_staff.create_one_data
    client.post(load_staff.base_url, json=data)
    response = client.post(load_staff.base_url, json=data)
    assert response.status_code == 400

def test_read_staff(client) -> None:
    data = load_staff.base_data[0]
    id = data["id"]
    response = client.get(f"{load_staff.base_url}{id}")
    assert response.status_code == 200

def test_read_staff_that_does_not_exist(client) -> None:
    response = client.get(f"{load_staff.base_url}999")
    assert response.status_code == 404


def test_update_staff(client) -> None:
    update_data = load_staff.update_one_data
    data = load_staff.base_data[0]
    id = data["id"]
    response = client.put(f"{load_staff.base_url}{id}", json=update_data)
    update_data["id"] = id
    assert response.status_code == 200
    assert response.json() == update_data

def test_update_staff_that_does_not_exist(client) -> None:
    update_data = load_staff.update_one_data
    response = client.put(f"{load_staff.base_url}999", json=update_data)
    assert response.status_code == 404

def test_delete_staff(client) -> None:
    data = load_staff.base_data[0]
    id = data["id"]
    response = client.delete(f"{load_staff.base_url}{id}")
    assert response.status_code == 200

def test_delete_staff_with_learning_journey(client) -> None:
    data = load_staff.base_data[1]
    id = data["id"]
    response = client.delete(f"{load_staff.base_url}{id}")
    assert response.status_code == 200

def test_delete_staff_with_registration(client) -> None:
    data = load_staff.base_data[0]
    id = data["id"]
    response = client.delete(f"{load_staff.base_url}{id}")
    assert response.status_code == 200

def test_delete_staff_with_learning_journey_and_registration(client) -> None:
    data = load_staff.base_data[2]
    id = data["id"]
    response = client.delete(f"{load_staff.base_url}{id}")
    assert response.status_code == 200

def test_delete_staff_that_does_not_exist(client) -> None:
    response = client.delete(f"{load_staff.base_url}999")
    assert response.status_code == 404

def test_read_staff_learning_journeys(client) -> None:
    data = load_staff.base_data[2]
    id = data["id"]
    learningjourney = load_learningjourney.base_data[0]
    response = client.get(f"{load_staff.base_url}{id}/learningjourneys")
    assert response.status_code == 200
    assert response.json()[0]['id'] == learningjourney["id"]

def test_read_staff_that_does_not_exist_learning_journeys(client) -> None:
    response = client.get(f"{load_staff.base_url}999/learningjourneys")
    assert response.status_code == 404

def test_read_staff_with_non_existing_learning_journey(client) -> None:
    data = load_staff.base_data[1]
    id = data["id"]
    response = client.get(f"{load_staff.base_url}{id}/learningjourneys")
    assert response.json() == []
