from .test_base import load_staff, load_learningjourney, load_jobrole, load_course, load_skill, load_registration
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
    assert response.json() == data


def test_read_staff_that_does_not_exist(client) -> None:
    response = client.get(f"{load_staff.base_url}999")
    assert response.status_code == 404


def test_update_staff(client) -> None:
    update_data = load_staff.update_one_data
    data = load_staff.base_data[0]
    id = data["id"]
    response = client.put(f"{load_staff.base_url}{id}", json=update_data)
    assert response.status_code == 200
    for key, value in update_data.items():
        assert response.json()[key] == value
    assert response.json()["id"] == id


def test_update_staff_that_does_not_exist(client) -> None:
    update_data = load_staff.update_one_data
    response = client.put(f"{load_staff.base_url}999", json=update_data)
    assert response.status_code == 404


def test_delete_staff(client) -> None:
    data = load_staff.base_data[1]
    id = data["id"]
    response = client.delete(f"{load_staff.base_url}{id}")
    assert response.status_code == 200


def test_delete_staff_with_learning_journey_only(client, session) -> None:
    data = load_staff.base_data[0]
    id = data["id"]
    response = client.delete(f"{load_staff.base_url}{id}")
    assert response.status_code == 200

    learningjourney_cleared = True
    for learningjourney in crud.learningjourney.get_multi(session):
        if learningjourney.staff_id == id:
            learningjourney_cleared = False
    assert learningjourney_cleared


def test_delete_staff_with_registration_only(client, session) -> None:
    data = load_staff.base_data[3]
    id = data["id"]
    response = client.delete(f"{load_staff.base_url}{id}")
    assert response.status_code == 200
    
    registration_cleared = True
    for registration in crud.registration.get_multi(session):
        if registration.staff_id == id:
            registration_cleared = False
    assert registration_cleared


def test_delete_staff_with_learning_journey_and_registration(client, session) -> None:
    data = load_staff.base_data[2]
    id = data["id"]
    response = client.delete(f"{load_staff.base_url}{id}")
    assert response.status_code == 200

    learningjourney_cleared = True
    for learningjourney in crud.learningjourney.get_multi(session):
        if learningjourney.staff_id == id:
            learningjourney_cleared = False
    assert learningjourney_cleared

    registration_cleared = True
    for registration in crud.registration.get_multi(session):
        if registration.staff_id == id:
            registration_cleared = False
    assert registration_cleared


def test_delete_staff_that_does_not_exist(client) -> None:
    response = client.delete(f"{load_staff.base_url}999")
    assert response.status_code == 404


def test_read_staff_learning_journeys(client) -> None:
    data = load_staff.base_data[2]
    id = data["id"]
    learningjourneys = load_learningjourney.base_data[0:2]
    response = client.get(f"{load_staff.base_url}{id}/learningjourneys")
    assert response.status_code == 200

    staff = load_staff.base_data[2]
    jobroles = load_jobrole.base_data[0:2]
    courses = [[course] for course in load_course.base_data[0:2]]
    skills = [[load_skill.base_data[0]], []]
    for i in range(len(learningjourneys)):
        for key, value in learningjourneys[i].items():
            assert response.json()[i][key] == value
        assert response.json()[i]["staff"] == staff
        assert response.json()[i]["jobrole"] == jobroles[i]
        for course in courses[i]:
            for key, value in course.items():
                assert response.json()[i]["courses"][0][key] == value
        assert response.json()[i]["courses"][0]["skills"] == skills[i]


def test_read_staff_that_does_not_exist_learning_journeys(client) -> None:
    response = client.get(f"{load_staff.base_url}999/learningjourneys")
    assert response.status_code == 404


def test_read_staff_with_no_learning_journeys(client) -> None:
    data = load_staff.base_data[1]
    id = data["id"]
    response = client.get(f"{load_staff.base_url}{id}/learningjourneys")
    assert response.json() == []


def test_get_completion_status_not_registered(client) -> None:
    course_id, staff_id = "COR001", 140002
    response = client.get(f"{load_staff.base_url}{staff_id}/courses/{course_id}/completion_status")
    assert response.json()['msg'] == "Not Registered"


def test_get_completion_status_rejected(client) -> None:
    data = load_registration.base_data[3]
    staff_id, course_id = data["staff_id"], data["course_id"]
    response = client.get(f"{load_staff.base_url}{staff_id}/courses/{course_id}/completion_status")
    assert response.json()['msg'] == "Registration Rejected"


def test_get_completion_status_waitlist(client) -> None:
    data = load_registration.base_data[2]
    staff_id, course_id = data["staff_id"], data["course_id"]
    response = client.get(f"{load_staff.base_url}{staff_id}/courses/{course_id}/completion_status")
    assert response.json()['msg'] == "Registration Waitlist"


def test_get_completion_status_ongoing(client) -> None:
    data = load_registration.base_data[4]
    staff_id, course_id = data["staff_id"], data["course_id"]
    response = client.get(f"{load_staff.base_url}{staff_id}/courses/{course_id}/completion_status")
    assert response.json()['msg'] == "Ongoing"


def test_get_completion_status_completed(client) -> None:
    data = load_registration.base_data[0]
    staff_id, course_id = data["staff_id"], data["course_id"]
    response = client.get(f"{load_staff.base_url}{staff_id}/courses/{course_id}/completion_status")
    assert response.json()['msg'] == "Completed"

def test_get_acquired_skills_for_jobrole(client) -> None:
    data = load_staff.base_data[2]
    staff_id = data["id"]
    jobrole_id = load_jobrole.base_data[0]["id"]
    skill = load_skill.base_data[0]
    response = client.get(f"{load_staff.base_url}{staff_id}/acquired_skills", params={"jobrole_id": jobrole_id})
    assert response.json() == skill

def test_get_acquired_skills_for_jobrole_that_staff_does_not_exist(client) -> None:
    jobrole_id = load_jobrole.base_data[0]["id"]
    response = client.get(f"{load_staff.base_url}999/acquired_skills", params={"jobrole_id": jobrole_id})
    assert response.status_code == 404

def test_get_acquired_skills_for_jobrole_that_jobrole_does_not_exist(client) -> None:
    data = load_staff.base_data[2]
    staff_id = data["id"]
    response = client.get(f"{load_staff.base_url}{staff_id}/acquired_skills", params={"jobrole_id": 999})
    assert response.status_code == 404

def test_get_acquired_skills_for_jobrole_that_jobrole_been_deleted(session, client) -> None:
    data = load_staff.base_data[2]
    staff_id = data["id"]
    jobrole_id = load_jobrole.base_data[0]["id"]
    crud.jobrole.remove(session, id=jobrole_id)
    response = client.get(f"{load_staff.base_url}{staff_id}/acquired_skills", params={"jobrole_id": jobrole_id})
    assert response.status_code == 404

def test_get_acquired_skills_for_jobrole_that_staff_has_no_registration(session, client) -> None:
    data = load_staff.base_data[2]
    staff_id = data["id"]
    jobrole_id = load_jobrole.base_data[0]["id"]

    crud.registration.remove(session, id=1)
    crud.registration.remove(session, id=3)
    crud.registration.remove(session, id=4)
    crud.registration.remove(session, id=6)
    
    response = client.get(f"{load_staff.base_url}{staff_id}/acquired_skills", params={"jobrole_id": jobrole_id})
    assert response.status_code == 404

def test_get_acquired_skills_for_jobrole_that_staff_has_no_completed_courses(session,client) -> None:
    data = load_staff.base_data[2]
    staff_id = data["id"]
    jobrole_id = load_jobrole.base_data[0]["id"]
    crud.registration.remove(session, id=1)
    response = client.get(f"{load_staff.base_url}{staff_id}/acquired_skills", params={"jobrole_id": jobrole_id})
    assert response.status_code == 404

def test_get_acquired_skills_for_jobrole_that_staff_has_no_acquired_skills_for_jobrole(client) -> None:
    data = load_staff.base_data[2]
    staff_id = data["id"]
    jobrole_id = load_jobrole.base_data[1]["id"]
    response = client.get(f"{load_staff.base_url}{staff_id}/acquired_skills", params={"jobrole_id": jobrole_id})
    assert response.status_code == 404