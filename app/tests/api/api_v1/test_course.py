from .test_base import load_course, load_skill
from app import crud


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
    data = load_course.base_data[0]
    id = data["id"]
    response = client.get(f"{load_course.base_url}{id}")
    assert response.status_code == 200
    for key, value in data.items():
        assert response.json()[key] == value
    assert response.json()["skills"][0]["id"] == 1


def test_update_course(client) -> None:
    update_data = load_course.update_one_data
    data = load_course.base_data[0]
    id = data["id"]
    response = client.put(f"{load_course.base_url}{id}", json=update_data)
    assert response.status_code == 200
    for key, value in update_data.items():
        assert response.json()[key] == value
    assert response.json()["id"] == id


def test_delete_course(client) -> None:
    data = load_course.base_data[3]
    id = data["id"]
    response = client.delete(f"{load_course.base_url}{id}")
    assert response.status_code == 200
    assert data not in response.json()


def test_create_course_that_exists(client) -> None:
    data = load_course.create_one_data
    client.post(load_course.base_url, json=data)
    response = client.post(load_course.base_url, json=data)
    assert response.status_code == 400


def test_read_course_that_does_not_exist(client) -> None:
    response = client.get(f"{load_course.base_url}999")
    assert response.status_code == 404


def test_update_course_that_does_not_exist(client) -> None:
    update_data = load_course.update_one_data
    response = client.put(f"{load_course.base_url}999", json=update_data)
    assert response.status_code == 404


def test_delete_course_that_does_not_exist(client) -> None:
    response = client.delete(f"{load_course.base_url}999")
    assert response.status_code == 404

def test_add_skill_to_course(client, session) -> None:
    data = load_course.base_data[1]
    id = data["id"]
    skill_ids = [load_skill.base_data[0]["id"]]
    response = client.post(
        f"{load_course.base_url}{id}/new_skills/",
        json=skill_ids)
    assert response.status_code == 200
    assert response.json() == [[],[]]
    inside = False
    for skill in crud.course.get(session, id=id).skills:
        if skill.id == skill_ids[0]:
            inside = True
            break
    assert inside

def test_add_skills_to_course(client, session) -> None:
    data = load_course.base_data[1]
    id = data["id"]
    skill_ids = [skill["id"] for skill in load_skill.base_data]
    response = client.post(
        f"{load_course.base_url}{id}/new_skills/",
        json=skill_ids)
    assert response.status_code == 200
    assert response.json() == [[],[]]
    all_in = True
    skill_ids_in_course ={skill.id for skill in crud.course.get(session, id=id).skills}
    for skill_id in skill_ids:
        if skill_id not in skill_ids_in_course:
            all_in = False
    assert all_in


def test_add_skills_to_course_that_does_not_exist(client) -> None:
    skill = load_skill.base_data[1]
    skill_ids = [skill["id"]]
    response = client.post(
        f"{load_course.base_url}999/new_skills/",
        json=skill_ids)
    assert response.status_code == 404


def test_add_skill_to_a_retired_course(client) -> None:
    data = load_course.base_data[2]
    id = data["id"]
    skill = load_skill.base_data[0]
    skill_ids = [skill["id"]]
    response = client.post(
        f"{load_course.base_url}{id}/new_skills/",
        json=skill_ids)
    assert response.status_code == 404


def test_add_skill_that_has_been_soft_deleted(client, session) -> None:
    data = load_course.base_data[1]
    id = data["id"]
    skill_ids = [skill["id"] for skill in load_skill.base_data]
    crud.skill.remove(session, id=skill_ids[0])
    response = client.post(
        f"{load_course.base_url}{id}/new_skills/",
        json=skill_ids)
    assert response.status_code == 200
    assert response.json() == [[load_skill.base_data[0]["skill_name"]],[]]
    all_in = True
    skill_ids_in_course ={skill.id for skill in crud.course.get(session, id=id).skills}
    for skill_id in skill_ids[1:]:
        if skill_id not in skill_ids_in_course:
            all_in = False
    assert all_in


def test_add_skill_to_course_that_already_has_it(client, session) -> None:
    data = load_course.base_data[0]
    id = data["id"]
    skill_ids = [skill["id"] for skill in load_skill.base_data]
    response = client.post(
        f"{load_course.base_url}{id}/new_skills/",
        json=skill_ids)
    assert response.status_code == 200
    assert response.json() == [[],[load_skill.base_data[0]["skill_name"]]]
    all_in = True
    skill_ids_in_course ={skill.id for skill in crud.course.get(session, id=id).skills}
    for skill_id in skill_ids:
        if skill_id not in skill_ids_in_course:
            all_in = False
    assert all_in


def test_delete_skill_from_course(client) -> None:
    data = load_course.base_data[0]
    id = data["id"]
    skill = load_skill.base_data[0]
    skill_id = skill["id"]
    response = client.delete(
        f"{load_course.base_url}{id}/delete_skill/{skill_id}",
    )
    assert response.status_code == 200
    for key, value in data.items():
        assert response.json()[key] == value
    assert skill not in response.json()["skills"]


def test_delete_skill_from_course_that_does_not_exist(client) -> None:
    skill = load_skill.base_data[0]
    skill_id = skill["id"]
    response = client.delete(
        f"{load_course.base_url}999/delete_skill/{skill_id}"
    )
    assert response.status_code == 404


def test_delete_skill_that_does_not_exist_from_course(client) -> None:
    data = load_course.base_data[0]
    id = data["id"]
    response = client.delete(
        f"{load_course.base_url}{id}/delete_skill/999"
    )
    assert response.status_code == 404


def test_delete_skill_that_is_not_associated_with_course(client) -> None:
    data = load_course.base_data[0]
    id = data["id"]
    skill = load_skill.base_data[1]
    skill_id = skill["id"]
    response = client.delete(
        f"{load_course.base_url}{id}/delete_skill/{skill_id}"
    )
    print(response.json()["detail"])
    assert response.status_code == 400


def test_get_skills_for_course(client) -> None:
    data = load_course.base_data[0]
    id = data["id"]
    skill = load_skill.base_data[0]
    response = client.get(f"{load_course.base_url}{id}/all_skills/")
    assert response.status_code == 200
    assert skill in response.json()


def test_get_skills_for_course_that_does_not_exist(client) -> None:
    response = client.get(f"{load_course.base_url}999/all_skills/")
    assert response.status_code == 404


def test_get_skills_for_a_retired_course(client) -> None:
    data = load_course.base_data[2]
    id = data["id"]
    response = client.get(f"{load_course.base_url}{id}/all_skills/")
    assert response.json() == []


def test_get_skills_for_course_that_has_no_skills(client) -> None:
    data = load_course.base_data[1]
    id = data["id"]
    response = client.get(f"{load_course.base_url}{id}/all_skills/")
    assert response.json() == []


def test_get_all_courses_with_their_skills(client) -> None:
    data = load_course.base_data
    response = client.get(f"{load_course.base_url}with_skills/")
    skill = load_skill.base_data[0]
    assert response.status_code == 200
    for i in range(len(data)):
        for key, value in data[i].items():
            assert response.json()[i][key] == value
    assert skill in response.json()[0]["skills"]
