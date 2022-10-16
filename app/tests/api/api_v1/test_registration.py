from .test_base import load_registration


def test_read_registrations(client) -> None: #read all registrations
    data = load_registration.base_data
    response = client.get(load_registration.base_url)
    assert response.status_code == 200
    assert response.json() == data

def test_create_registration(client) -> None:
    data = load_registration.create_one_data
    response = client.post(load_registration.base_url, json=data)
    assert response.status_code == 200
    assert response.json() == data


def test_read_registration(client) -> None: #read one registration
    data = load_registration.base_data[0]
    id = data["id"]
    response = client.get(f"{load_registration.base_url}{id}")
    assert response.status_code == 200
    assert response.json() == data


def test_update_registration(client) -> None:
    update_data = load_registration.update_one_data
    data = load_registration.base_data[0]
    id = data["id"]
    response = client.put(f"{load_registration.base_url}{id}", json=update_data)
    update_data["id"] = id
    assert response.status_code == 200
    assert response.json() == update_data

def test_delete_registration(client) -> None:
    data = load_registration.base_data[0]
    id = data["id"]
    response = client.delete(f"{load_registration.base_url}{id}")
    assert response.status_code == 200
    assert data not in response.json()


#The registration with this registration id already exists in the system.
def test_create_registration_that_exists(client) -> None:
    data = load_registration.create_one_data
    response = client.post(load_registration.base_url, json=data)
    assert response.status_code == 400

#Registration not found
def test_read_registration_that_does_not_exist(client) -> None:
    response = client.get(f"{load_registration.base_url}999")
    assert response.status_code == 404

#Registration not found in the system for update
def test_update_registration_that_does_not_exist(client) -> None:
    update_data = load_registration.update_one_data
    response = client.put(f"{load_registration.base_url}999", json=update_data)
    assert response.status_code == 404

#Registration not found in the system for delete
def test_delete_registration_that_does_not_exist(client) -> None:
    response = client.delete(f"{load_registration.base_url}999")
    assert response.status_code == 404
