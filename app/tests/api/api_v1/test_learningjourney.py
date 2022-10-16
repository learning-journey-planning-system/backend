from .test_base import load_learningjourney, load_course, load_skill


def test_read_learningjourneys(client) -> None:
    data = load_learningjourney.base_data
    response = client.get(load_learningjourney.base_url)
    assert response.status_code == 200
    assert response.json() == data


def test_create_learningjourney(client) -> None:
    data = load_learningjourney.create_one_data
    response = client.post(load_learningjourney.base_url, json=data)
    assert response.status_code == 200
    assert response.json()["staff_id"] == data["staff_id"]
    assert response.json()["jobrole_id"] == data["jobrole_id"]


def test_create_learningjourney_that_exists(client) -> None:
    data = load_learningjourney.create_one_data
    client.post(load_learningjourney.base_url, json=data)
    response = client.post(load_learningjourney.base_url, json=data)
    assert response.status_code == 400


def test_read_learningjourney(client) -> None:
    data = load_learningjourney.base_data[0]
    id = data["id"]
    response = client.get(f"{load_learningjourney.base_url}{id}")
    assert response.status_code == 200
    for key, value in data.items():
        assert response.json()[key] == value
    
    course = load_course.base_data[0]
    skills = [load_skill.base_data[0]]
    assert len(response.json()["courses"]) == 1
    for key, value in course.items():
        assert response.json()["courses"][0][key] == value
    assert response.json()["courses"][0]["skills"] == skills


def test_read_learningjourney_that_does_not_exist(client) -> None:
    response = client.get(f"{load_learningjourney.base_url}999")
    assert response.status_code == 404


def test_update_learningjourney(client) -> None:
    update_data = load_learningjourney.update_one_data
    data = load_learningjourney.base_data[0]
    id = data["id"]
    response = client.put(f"{load_learningjourney.base_url}{id}", json=update_data)
    assert response.status_code == 200
    for key, value in update_data.items():
        assert response.json()[key] == value
    assert response.json()["id"] == id


def test_update_learningjourney_that_does_not_exist(client) -> None:
    update_data = load_learningjourney.update_one_data
    response = client.put(f"{load_learningjourney.base_url}999", json=update_data)
    assert response.status_code == 404


def test_delete_learningjourney(client) -> None:
    data = load_learningjourney.base_data[0]
    id = data["id"]
    response = client.delete(f"{load_learningjourney.base_url}{id}")
    assert response.status_code == 200
    assert data not in response.json()


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


def test_add_course_to_learningjourney_that_does_not_exist(client) -> None:
    course = load_course.base_data[1]
    course_id = course["id"]
    response = client.post(f"{load_learningjourney.base_url}999/new_course/", params={"course_id": course_id})
    assert response.status_code == 404


def test_add_non_existent_course_to_learningjourney(client) -> None:
    data = load_learningjourney.base_data[0]
    id = data["id"]
    response = client.post(f"{load_learningjourney.base_url}{id}/new_course/", params={"course_id": "999"})
    assert response.status_code == 404


def test_add_course_already_in_learningjourney_to_it(client) -> None:
    data = load_learningjourney.base_data[0]
    id = data["id"]
    course = load_course.base_data[0]
    course_id = course["id"]
    response = client.post(f"{load_learningjourney.base_url}{id}/new_course/", params={"course_id": course_id})
    assert response.status_code == 400


def test_delete_course_from_learningjourney(client) -> None:
    data = load_learningjourney.base_data[0]
    id = data["id"]
    course = load_course.base_data[0]
    course_id = course["id"]
    response = client.delete(f"{load_learningjourney.base_url}{id}/delete_course/{course_id}")
    assert response.status_code == 200
    assert course not in response.json()["courses"]


def test_delete_course_from_learningjourney_that_does_not_exist(client) -> None:
    course_id = load_course.base_data[0]["id"]
    response = client.delete(f"{load_learningjourney.base_url}999/delete_course/{course_id}")
    assert response.status_code == 404


def test_delete_non_existent_course_from_learningjourney(client) -> None:
    data = load_learningjourney.base_data[0]
    id = data["id"]
    response = client.delete(f"{load_learningjourney.base_url}{id}/delete_course/999")
    assert response.status_code == 404


def test_delete_course_that_does_not_exist_in_learningjourney(client) -> None:
    data = load_learningjourney.base_data[0]
    id = data["id"]
    course_id = load_course.base_data[1]["id"]
    response = client.delete(f"{load_learningjourney.base_url}{id}/delete_course/{course_id}")
    assert response.status_code == 400



