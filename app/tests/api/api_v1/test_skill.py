from .test_base import load_skill, load_course, load_registration
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
    data = load_skill.base_data[0]
    id = data["id"]
    update_data = {"skill_name": "new name"}
    response = client.put(f"{load_skill.base_url}{id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["skill_name"] == update_data["skill_name"]

def test_update_skill_which_skill_that_does_not_exist(client) -> None:
    update_data = {"skill_name": "new name"}
    response = client.put(f"{load_skill.base_url}999", json=update_data)
    assert response.status_code == 404

def test_update_skill_which_skill_that_has_been_deleted(client,session) -> None:
    crud.skill.remove(session, id=1)
    update_data = {"skill_name": "new name"}
    response = client.put(f"{load_skill.base_url}1", json=update_data)
    assert response.status_code == 404

def test_update_skill_which_skill_name_is_same_as_current(client) -> None:
    update_data = {"skill_name": "Web Design"}
    response = client.put(f"{load_skill.base_url}1", json=update_data)
    assert response.status_code == 404

def test_update_skill_which_skill_name_exist_in_db(client) -> None:
    update_data = {"skill_name": "Data Analysis"}
    response = client.put(f"{load_skill.base_url}1", json=update_data)
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
    data = load_skill.base_data[0]
    skill_id = data["id"]
    crud.skill.remove(session, id=skill_id)
    response = client.delete(f"{load_skill.base_url}{skill_id}")
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
    data = load_skill.base_data[4]
    id = data["id"]
    response = client.get(f"{load_skill.base_url}{id}/courses/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_available_skills(client, session) -> None:

    # delete one skill record
    delete_id = load_skill.base_data[0]["id"]
    crud.skill.remove(session, id=delete_id)

    # load the rest of the records
    data = load_skill.base_data[1:]
    response = client.get(f"{load_skill.base_url}available/")

    # check the response
    assert response.status_code == 200

    # check if the rest of the records are in the response
    assert response.json() == data


def test_get_courses_with_completion_status_completed_for_skill(client) -> None:
    staff_id = load_registration.base_data[0]["staff_id"]
    course = load_course.base_data[0]
    response = client.get(f"{load_skill.base_url}1/courses_with_completion/", params={"staff_id": staff_id})
    assert response.status_code == 200
    for key, value in course.items():
        assert response.json()[0][key] == value
    assert response.json()[0]["completion_status"] == "Completed"


def test_get_courses_with_completion_status_waitlist_for_skill(client) -> None:
    staff_id = load_registration.base_data[0]["staff_id"]
    course = load_course.base_data[5]
    response = client.get(f"{load_skill.base_url}2/courses_with_completion/", params={"staff_id": staff_id})
    assert response.status_code == 200
    for key, value in course.items():
        assert response.json()[0][key] == value
    assert response.json()[0]["completion_status"] == "Registration Waitlist"


def test_get_courses_with_completion_status_rejected_for_skill(client) -> None:
    staff_id = load_registration.base_data[0]["staff_id"]
    course = load_course.base_data[3]
    response = client.get(f"{load_skill.base_url}3/courses_with_completion/", params={"staff_id": staff_id})
    assert response.status_code == 200
    for key, value in course.items():
        assert response.json()[0][key] == value
    assert response.json()[0]["completion_status"] == "Registration Rejected"


def test_get_courses_with_completion_status_ongoing_for_skill(client) -> None:
    staff_id = load_registration.base_data[0]["staff_id"]
    course = load_course.base_data[4]
    response = client.get(f"{load_skill.base_url}4/courses_with_completion/", params={"staff_id": staff_id})
    assert response.status_code == 200
    for key, value in course.items():
        assert response.json()[0][key] == value
    assert response.json()[0]["completion_status"] == "Ongoing"


def test_get_courses_with_completion_status_not_registered_for_skill(client) -> None:
    staff_id = load_registration.base_data[0]["staff_id"]
    course = load_course.base_data[6]
    response = client.get(f"{load_skill.base_url}6/courses_with_completion/", params={"staff_id": staff_id})
    assert response.status_code == 200
    print(response.json())
    for key, value in course.items():
        assert response.json()[0][key] == value
    assert response.json()[0]["completion_status"] == "Not Registered"