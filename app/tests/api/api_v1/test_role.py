from .test_base import load_role

def test_read_roles(client) -> None:
    data = load_role.base_data
    response = client.get(load_role.base_url)
    assert response.status_code == 200
    assert response.json() == data

def test_create_role(client) -> None:
    data = load_role.create_one_data
    response = client.post(load_role.base_url, json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_create_role_that_exists(client) -> None:
    data = load_role.create_one_data
    client.post(load_role.base_url, json=data)
    response = client.post(load_role.base_url, json=data)
    assert response.status_code == 400

def test_read_role(client) -> None:
    data = load_role.base_data[0]
    id = data["id"]
    response = client.get(f"{load_role.base_url}{id}")
    assert response.status_code == 200

def test_read_role_that_does_not_exist(client) -> None:
    response = client.get(f"{load_role.base_url}999")
    assert response.status_code == 404

def test_update_role(client) -> None:
    update_data = load_role.update_one_data
    data = load_role.base_data[0]
    id = data["id"]
    response = client.put(f"{load_role.base_url}{id}", json=update_data)
    update_data["id"] = id
    assert response.status_code == 200
    assert response.json() == update_data

def test_update_role_that_does_not_exist(client) -> None:
    update_data = load_role.update_one_data
    response = client.put(f"{load_role.base_url}999", json=update_data)
    assert response.status_code == 404

