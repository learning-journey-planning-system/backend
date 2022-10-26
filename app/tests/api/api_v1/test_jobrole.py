from app.schemas import skill
from .test_base import load_skill, load_jobrole, load_course
from app import crud


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


def test_create_jobrole_that_exists_already(client) -> None:
    jobrole_name = load_jobrole.base_data[0]["jobrole_name"]
    response = client.post(load_jobrole.base_url, json={"jobrole_name": jobrole_name})
    assert response.status_code == 400


def test_read_jobrole(client) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    skill = load_skill.base_data[0]
    course = load_course.base_data[0]
    response = client.get(f"{load_jobrole.base_url}{id}")
    assert response.status_code == 200
    for key, value in data.items():
        assert response.json()[key] == value
    assert len(response.json()["skills"]) == 1
    for key, value in skill.items():
        assert response.json()["skills"][0][key] == value
    assert len(response.json()["skills"][0]["courses"]) == 1
    for key, value in course.items():
        assert response.json()["skills"][0]["courses"][0][key] == value


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

def test_update_jobrole_that_is_already_deleted(client, session) -> None:
    crud.jobrole.remove(session, id=1)
    update_data = load_jobrole.update_one_data
    response = client.put(f"{load_jobrole.base_url}1", json=update_data)
    assert response.status_code == 400

def test_update_jobrole_which_jobrole_name_is_same_as_current(client) -> None:
    update_data = {"jobrole_name": "Operations Executive"}
    response = client.put(f"{load_jobrole.base_url}1", json=update_data)
    assert response.status_code == 404

def test_update_jobrole_which_jobrole_name_exist_in_db(client) -> None:
    update_data = {"jobrole_name": "Business Analyst"}
    response = client.put(f"{load_jobrole.base_url}1", json=update_data)
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


def test_add_skill_to_jobrole(client, session) -> None:
    data = load_jobrole.base_data[1]
    id = data["id"]
    skill_ids = [load_skill.base_data[0]["id"]]
    response = client.post(
        f"{load_jobrole.base_url}{id}/new_skills/",
        json=skill_ids)
    assert response.status_code == 200
    assert response.json() == [[],[]]
    inside = False
    for skill in crud.jobrole.get(session, id=id).skills:
        if skill.id == skill_ids[0]:
            inside = True
            break
    assert inside


def test_add_skills_to_jobrole(client, session) -> None:
    data = load_jobrole.base_data[1]
    id = data["id"]
    skill_ids = [skill["id"] for skill in load_skill.base_data]
    response = client.post(
        f"{load_jobrole.base_url}{id}/new_skills/",
        json=skill_ids)
    assert response.status_code == 200
    assert response.json() == [[],[]]
    all_in = True
    skill_ids_in_jobrole ={skill.id for skill in crud.jobrole.get(session, id=id).skills}
    for skill_id in skill_ids:
        if skill_id not in skill_ids_in_jobrole:
            all_in = False
    assert all_in


def test_add_skill_to_jobrole_that_does_not_exist(client) -> None:
    skill = load_skill.base_data[1]
    skill_ids = [skill["id"]]
    response = client.post(
        f"{load_jobrole.base_url}999/new_skill/", 
        json=skill_ids)
    assert response.status_code == 404


def test_add_skill_to_jobrole_that_been_softdeleted(client, session) -> None:
    crud.jobrole.remove(session, id=1)
    skill = load_skill.base_data[0]
    skill_ids = [skill["id"]]
    response = client.post(
        f"{load_jobrole.base_url}1/new_skill/", 
        json=skill_ids)
    assert response.status_code == 404


def test_add_softdeleted_skill_to_jobrole(client, session) -> None:
    data = load_jobrole.base_data[1]
    id = data["id"]
    skill_ids = [skill["id"] for skill in load_skill.base_data]
    crud.skill.remove(session, id=skill_ids[0])
    response = client.post(
        f"{load_jobrole.base_url}{id}/new_skills/",
        json=skill_ids)
    assert response.status_code == 200
    assert response.json() == [[load_skill.base_data[0]["skill_name"]],[]]
    all_in = True
    skill_ids_in_jobrole ={skill.id for skill in crud.jobrole.get(session, id=id).skills}
    for skill_id in skill_ids[1:]:
        if skill_id not in skill_ids_in_jobrole:
            all_in = False
    assert all_in


def test_add_skill_to_jobrole_that_already_exists(client, session) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    skill_ids = [skill["id"] for skill in load_skill.base_data]
    response = client.post(
        f"{load_jobrole.base_url}{id}/new_skills/",
        json=skill_ids)
    assert response.status_code == 200
    assert response.json() == [[],[load_skill.base_data[0]["skill_name"]]]
    all_in = True
    skill_ids_in_jobrole ={skill.id for skill in crud.jobrole.get(session, id=id).skills}
    for skill_id in skill_ids:
        if skill_id not in skill_ids_in_jobrole:
            all_in = False
    assert all_in


def test_get_skills_for_jobrole(client) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    skills = [load_skill.base_data[0]]
    response = client.get(f"{load_jobrole.base_url}{id}/skills/")
    assert response.status_code == 200
    assert response.json() == skills


def test_get_skills_for_jobrole_that_does_not_exist(client) -> None:
    response = client.get(f"{load_jobrole.base_url}999/skills/")
    assert response.status_code == 404


def test_get_available_jobroles(client, session) -> None:

    # delete one jobrole record
    delete_id = load_jobrole.base_data[0]["id"]
    delete_jobrole = load_jobrole.base_data[0]
    crud.jobrole.remove(session, id=delete_id)

    # load the rest of the records
    data = load_jobrole.base_data[1:]
    response = client.get(f"{load_jobrole.base_url}available/")

    # check the response
    assert response.status_code == 200

    # check if all required data is in the response
    for i in range(len(data)):
        for key, value in data[i].items():
            assert response.json()[i][key] == value
            assert response.json()[i]["skills"] == []

    # check if soft deleted record is not in the response
    inside = False
    for record in response.json():
        if record["id"] == delete_id:
            inside = True
    assert not inside


def test_get_available_skills_for_jobrole(client, session) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    skills = [load_skill.base_data[0]]
    response = client.get(f"{load_jobrole.base_url}{id}/available_skills/")
    assert response.status_code == 200
    assert response.json() == skills

    crud.skill.remove(session, id=skills[0]["id"])
    response = client.get(f"{load_jobrole.base_url}{id}/available_skills/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_available_skills_for_jobrole_that_does_not_exist(client) -> None:
    response = client.get(f"{load_jobrole.base_url}999/available_skills/")
    assert response.status_code == 404


def test_delete_skill_from_jobrole(client) -> None:
    data = load_jobrole.base_data[0]
    print(data)
    id = data["id"]
    skill_id = load_skill.base_data[0]["id"]
    response = client.delete(f"{load_jobrole.base_url}{id}/delete_skill/{skill_id}")
    assert response.status_code == 200
    print(response.json())
    for key, value in data.items():
        assert response.json()[key] == value
    assert skill not in response.json()["skills"]


def test_delete_skill_from_jobrole_that_does_not_exist(client) -> None:
    skill_id = load_skill.base_data[0]['id']
    response = client.delete(f"{load_jobrole.base_url}999/delete_skill/{skill_id}")
    assert response.status_code == 404


def test_delete_skill_from_jobrole_that_been_softdeleted(client, session) -> None:
    crud.jobrole.remove(session, id=1)
    skill_id = load_skill.base_data[0]['id']
    response = client.delete(f"{load_jobrole.base_url}1/delete_skill/{skill_id}")
    assert response.status_code == 404


def test_delete_skill_that_does_not_exist_from_jobrole(client) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    response = client.delete(f"{load_jobrole.base_url}{id}/delete_skill/999")
    assert response.status_code == 404


def test_delete_skill_that_been_softdeleted_from_jobrole(client, session) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    skill_id = load_skill.base_data[0]["id"]
    crud.skill.remove(session, id=skill_id)
    response = client.delete(f"{load_jobrole.base_url}{id}/delete_skill/{skill_id}")
    assert response.status_code == 404


def test_delete_skill_that_is_not_in_jobrole(client) -> None:
    data = load_jobrole.base_data[0]
    id = data["id"]
    skill_id = load_skill.base_data[1]["id"]
    response = client.delete(f"{load_jobrole.base_url}{id}/delete_skill/{skill_id}")
    assert response.status_code == 400

