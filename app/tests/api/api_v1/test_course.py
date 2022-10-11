from app.tests.utils.utils import random_num_in, random_num_out
from .test_base import LoadDataBase

load_course = LoadDataBase("course")

def test_read_courses(client) -> None:
    data = load_course.base_data
    response = client.get(load_course.base_url)
    assert response.status_code == 200
    assert response.json() == data

def test_create_course(client) -> None:
    data = load_course.create_one_data
    response = client.post(load_course.base_url, json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_read_course(client) -> None:
    data = load_course.base_data
    rand_record = random_num_in(len(data))
    id = data[rand_record]["id"]
    response = client.get(f"{load_course.base_url}{id}")
    data[rand_record]["skills"] = []
    assert response.status_code == 200
    assert response.json() == data[rand_record]

def test_update_course(client) -> None:
    update_data = load_course.update_one_data
    data = load_course.base_data
    rand_record = random_num_in(len(data))
    id = data[rand_record]["id"]
    response = client.put(f"{load_course.base_url}{id}", json=update_data)
    update_data["id"] = id
    assert response.status_code == 200
    assert response.json() == update_data

def test_delete_course(client) -> None:
    data = load_course.base_data
    rand_record = random_num_in(len(data))
    id = data[rand_record]["id"]
    response = client.delete(f"{load_course.base_url}{id}")
    assert response.status_code == 200
    assert data[rand_record] not in response.json()

def test_create_course_that_exists(client) -> None:
    data = load_course.create_one_data
    client.post(load_course.base_url, json=data)
    response = client.post(load_course.base_url, json=data)
    assert response.status_code == 400

def test_read_course_that_does_not_exist(client) -> None:
    data = load_course.base_data
    rand_record = random_num_out(len(data))
    response = client.get(f"{load_course.base_url}{rand_record}")
    assert response.status_code == 404

def test_update_course_that_does_not_exist(client) -> None:
    update_data = load_course.update_one_data
    data = load_course.base_data
    rand_record = random_num_out(len(data))
    response = client.put(f"{load_course.base_url}{rand_record}", json=update_data)
    assert response.status_code == 404

def test_delete_course_that_does_not_exist(client) -> None:
    data = load_course.base_data
    rand_record = random_num_out(len(data))
    response = client.delete(f"{load_course.base_url}{rand_record}")
    assert response.status_code == 404

# def test_add_skill_to_course(client) -> None:
#     data = load_course.base_data
#     rand_record = random_num_in(len(data))
#     id = data[rand_record]["id"]
#     response = client.post(f"{load_course.base_url}{id}/new_skill/", json={"skill_id": "1"})
#     assert response.status_code == 200
#     assert response.json() == data[rand_record]
