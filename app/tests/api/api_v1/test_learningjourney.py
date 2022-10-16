from .test_course import load_course
from .test_jobrole import load_jobrole
from .test_staff import load_staff
from .test_base import LoadDataBase
from app import crud

load_learningjourney = LoadDataBase("learningjourney")

def test_read_learningjourneys(client) -> None:
    data = load_learningjourney.base_data
    response = client.get(load_learningjourney.base_url)
    assert response.status_code == 200
    assert response.json() == data

def test_create_learningjourney(client) -> None:
    data = load_learningjourney.create_one_data
    response = client.post(load_learningjourney.base_url, json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_read_learningjourney(client) -> None:
    data = load_learningjourney.base_data[0]
    id = data["id"]
    response = client.get(f"{load_learningjourney.base_url}{id}")
    assert response.status_code == 200
    for key, value in data.items():
        assert response.json()[key] == value
    assert response.json()["staff"]["id"] == 140001
    assert response.json()["jobrole"]["id"] == 11
    assert response.json()["courses"][0]["id"] == 'FIN001'

def test_update_learningjourney(client) -> None:
    update_data = load_learningjourney.update_one_data
    data = load_learningjourney.base_data[0]
    id = data["id"]
    response = client.put(f"{load_learningjourney.base_url}{id}", json=update_data)
    update_data["id"] = id
    assert response.status_code == 200
    assert response.json() == update_data

def test_delete_learningjourney(client) -> None:
    data = load_learningjourney.base_data[0]
    id = data["id"]
    response = client.delete(f"{load_learningjourney.base_url}{id}")
    assert response.status_code == 200
    assert data not in response.json()

#The learning journey with this staff_id and jobrole_id already exists in the system.
def test_create_learningjourney_that_exists(client) -> None:
    data = load_learningjourney.create_one_data
    client.post(load_learningjourney.base_url, json=data)
    response = client.post(load_learningjourney.base_url, json=data)
    assert response.status_code == 400

#Learning Journey not found
def test_read_learningjourney_that_does_not_exist(client) -> None:
    response = client.get(f"{load_learningjourney.base_url}999")
    assert response.status_code == 404

#Learning Journey not found for update
def test_update_learningjourney_that_does_not_exist(client) -> None:
    update_data = load_learningjourney.update_one_data
    response = client.put(f"{load_learningjourney.base_url}999", json=update_data)
    assert response.status_code == 404

#Learning Journey not found for delete
def test_delete_learningjourney_that_does_not_exist(client) -> None:
    response = client.delete(f"{load_learningjourney.base_url}999")
    assert response.status_code == 404

def test_add_course_to_learningjourney(client) -> None:
    data = load_learningjourney.base_data[0]
    id = data["id"]
    course = load_course.base_data[1]
    course_id = course["id"]
    response = client.post(f"{load_learningjourney.base_url}{id}/new_course/", params={"course_id": course_id})
    assert response.status_code == 200
    assert course in response.json()["courses"]

#Learning Journey not found
def test_add_course_to_learningjourney_that_does_not_exist(client) -> None:
    course = load_course.base_data[1]
    course_id = course["id"]
    response = client.post(f"{load_learningjourney.base_url}999/new_course/", params={"course_id": course_id})
    assert response.status_code == 404

#The course is already in the learning journey
def test_add_course_to_learningjourney_that_already_exists(client) -> None:
    data = load_learningjourney.base_data[0]
    id = data["id"]
    course = load_course.base_data[3]
    course_id = course["id"]
    response = client.post(f"{load_learningjourney.base_url}{id}/new_course/", params={"course_id": course_id})
    assert response.status_code == 400

#Course not found
def test_add_non_existent_course_to_learningjourney(client) -> None:
    data = load_learningjourney.base_data[0]
    id = data["id"]
    response = client.post(f"{load_learningjourney.base_url}{id}/new_course/", params={"course_id": "999"})
    assert response.status_code == 404

def test_delete_course_from_learningjourney(client) -> None:
    data = load_learningjourney.base_data[0]
    id = data["id"]
    course = load_course.base_data[3]
    course_id = course["id"]
    response = client.delete(f"{load_learningjourney.base_url}{id}/delete_course/", params={"course_id": course_id})
    assert response.status_code == 200
    assert course not in response.json()["courses"]

#Learning Journey not found
def test_delete_course_from_learningjourney_that_does_not_exist(client) -> None:
    course = load_course.base_data[3]
    course_id = course["id"]
    response = client.delete(f"{load_learningjourney.base_url}999/delete_course/", params={"course_id": course_id})
    assert response.status_code == 404

#Course not found
def test_delete_non_existent_course_from_learningjourney(client) -> None:
    data = load_learningjourney.base_data[0]
    id = data["id"]
    response = client.delete(f"{load_learningjourney.base_url}{id}/delete_course/", params={"course_id": "999"})
    assert response.status_code == 404

#Course not in learning journey
def test_delete_course_that_does_not_exist_in_learningjourney(client) -> None:
    data = load_learningjourney.base_data[0]
    id = data["id"]
    course = load_course.base_data[0]
    course_id = course["id"]
    response = client.delete(f"{load_learningjourney.base_url}{id}/delete_course/", params={"course_id": course_id})
    assert response.status_code == 400



