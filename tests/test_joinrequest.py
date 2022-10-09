import requests
import json

def test_create_join_request():
    response = requests.post('http://127.0.0.1:5000/user/', json={
        "username": "john",
        "password": "1234",
        "about": {
            "name": "john",
            "email": "john@john.john",
            "phone": "555-5555",
            "bio": "my name is john",
        }
    })
    response_body = response.json()
    user_id_1 = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/user/', json={
        "username": "johnny",
        "password": "12345",
        "about": {
            "name": "johnny",
            "email": "johnny@johnny.johnny",
            "phone": "555-5556",
            "bio": "my name is johnny!!!",
        }
    })
    response_body = response.json()
    user_id_2 = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/project/', json={
        "creator": user_id_1
    })
    response_body = response.json()
    project_id = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/team/', json={
        "creator": user_id_1,
        "project": project_id,
    })
    response_body = response.json()
    team_id = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/join_request/', json={
        "creator": user_id_2,
        "team": team_id
    })
    assert response.status_code == 200
    fake_team_id = '__________'
    fake_user_id = '__________'
    response = requests.post('http://127.0.0.1:5000/join_request/', json={
        "creator": user_id_2,
        "team": fake_team_id
    })
    assert response.content == b'Not Found'
    assert response.status_code == 404
    response = requests.post('http://127.0.0.1:5000/join_request/', json={
        "creator": fake_user_id,
        "team": team_id,
    })
    assert response.content == b'Not Found'
    assert response.status_code == 404


def test_get_join_request():
    response = requests.post('http://127.0.0.1:5000/user/', json={
        "username": "john",
        "password": "1234",
        "about": {
            "name": "john",
            "email": "john@john.john",
            "phone": "555-5555",
            "bio": "my name is john",
        }
    })
    response_body = response.json()
    user_id_1 = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/user/', json={
        "username": "johnny",
        "password": "12345",
        "about": {
            "name": "johnny",
            "email": "johnny@johnny.johnny",
            "phone": "555-5556",
            "bio": "my name is johnny!!!",
        }
    })
    response_body = response.json()
    user_id_2 = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/project/', json={
        "creator": user_id_1
    })
    response_body = response.json()
    project_id = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/team/', json={
        "creator": user_id_1,
        "project": project_id,
    })
    response_body = response.json()
    team_id = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/join_request/', json={
        "creator": user_id_2,
        "team": team_id
    })
    response_body = response.json()
    join_request_id = str(response_body["id"])

    fake_join_request_id = '__________'
    response = requests.get(f'http://127.0.0.1:5000/join_request/{join_request_id}/')
    responsenew = response.content.decode("utf-8")
    response_body = json.loads(responsenew)
    assert response_body == {
    "join_request": {
        "id": join_request_id,
        "status": "pending",
        "team": team_id,
        "user": user_id_2
    }
    }

    assert response.status_code == 200
    response = requests.get(f'http://127.0.0.1:5000/join_request/{fake_join_request_id}/')
    assert response.content == b'Not Found'
    assert response.status_code == 404


def test_accept_join_request():
    response = requests.post('http://127.0.0.1:5000/user/', json={
        "username": "john",
        "password": "1234",
        "about": {
            "name": "john",
            "email": "john@john.john",
            "phone": "555-5555",
            "bio": "my name is john",
        }
    })
    response_body = response.json()
    user_id_1 = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/user/', json={
        "username": "johnny",
        "password": "12345",
        "about": {
            "name": "johnny",
            "email": "johnny@johnny.johnny",
            "phone": "555-5556",
            "bio": "my name is johnny!!!",
        }
    })
    response_body = response.json()
    user_id_2 = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/project/', json={
        "creator": user_id_1
    })
    response_body = response.json()
    project_id = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/team/', json={
        "creator": user_id_1,
        "project": project_id,
    })
    response_body = response.json()
    team_id = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/join_request/', json={
        "creator": user_id_2,
        "team": team_id
    })
    response_body = response.json()
    join_request_id = str(response_body["id"])

    fake_join_request_id = '__________'
    response = requests.patch(f'http://127.0.0.1:5000/join_request/{join_request_id}/accept/')
    assert response.status_code == 200
    response = requests.get(f'http://127.0.0.1:5000/join_request/{join_request_id}/')
    responsenew = response.content.decode("utf-8")
    response_body = json.loads(responsenew)
    assert response_body == {
    "join_request": {
        "id": join_request_id,
        "status": "accepted",
        "team": team_id,
        "user": user_id_2
    }
    }
    response = requests.patch(f'http://127.0.0.1:5000/join_request/{join_request_id}/accept/')
    assert response.content == b'Conflict'
    assert response.status_code == 409

    response = requests.patch(f'http://127.0.0.1:5000/join_request/{fake_join_request_id}/accept/')
    assert response.content == b'Not Found'
    assert response.status_code == 404


def test_reject_join_request():
    response = requests.post('http://127.0.0.1:5000/user/', json={
        "username": "john",
        "password": "1234",
        "about": {
            "name": "john",
            "email": "john@john.john",
            "phone": "555-5555",
            "bio": "my name is john",
        }
    })
    response_body = response.json()
    user_id_1 = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/user/', json={
        "username": "johnny",
        "password": "12345",
        "about": {
            "name": "johnny",
            "email": "johnny@johnny.johnny",
            "phone": "555-5556",
            "bio": "my name is johnny!!!",
        }
    })
    response_body = response.json()
    user_id_2 = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/project/', json={
        "creator": user_id_1
    })
    response_body = response.json()
    project_id = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/team/', json={
        "creator": user_id_1,
        "project": project_id,
    })
    response_body = response.json()
    team_id = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/join_request/', json={
        "creator": user_id_2,
        "team": team_id
    })
    response_body = response.json()
    join_request_id = str(response_body["id"])
    fake_join_request_id = '__________'
    response = requests.patch(f'http://127.0.0.1:5000/join_request/{join_request_id}/reject/')
    assert response.status_code == 200
    response = requests.get(f'http://127.0.0.1:5000/join_request/{join_request_id}/')
    responsenew = response.content.decode("utf-8")
    response_body = json.loads(responsenew)
    assert response_body == {
    "join_request": {
        "id": join_request_id,
        "status": "rejected",
        "team": team_id,
        "user": user_id_2
    }
    }
    response = requests.patch(f'http://127.0.0.1:5000/join_request/{join_request_id}/reject/')
    assert response.content == b'Conflict'
    assert response.status_code == 409
    response = requests.patch(f'http://127.0.0.1:5000/join_request/{fake_join_request_id}/reject/')
    assert response.content == b'Not Found'
    assert response.status_code == 404


def test_withdraw_join_request():
    response = requests.post('http://127.0.0.1:5000/user/', json={
        "username": "john",
        "password": "1234",
        "about": {
            "name": "john",
            "email": "john@john.john",
            "phone": "555-5555",
            "bio": "my name is john",
        }
    })
    response_body = response.json()
    user_id_1 = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/user/', json={
        "username": "johnny",
        "password": "12345",
        "about": {
            "name": "johnny",
            "email": "johnny@johnny.johnny",
            "phone": "555-5556",
            "bio": "my name is johnny!!!",
        }
    })
    response_body = response.json()
    user_id_2 = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/project/', json={
        "creator": user_id_1
    })
    response_body = response.json()
    project_id = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/team/', json={
        "creator": user_id_1,
        "project": project_id,
    })
    response_body = response.json()
    team_id = str(response_body["id"])
    response = requests.post('http://127.0.0.1:5000/join_request/', json={
        "creator": user_id_2,
        "team": team_id
    })
    response_body = response.json()
    join_request_id = str(response_body["id"])
    fake_join_request_id = '__________'
    response = requests.patch(f'http://127.0.0.1:5000/join_request/{join_request_id}/withdraw/')
    assert response.status_code == 200
    response = requests.get(f'http://127.0.0.1:5000/join_request/{join_request_id}/')
    responsenew = response.content.decode("utf-8")
    response_body = json.loads(responsenew)
    assert response_body == {
    "join_request": {
        "id": join_request_id,
        "status": "withdrawn",
        "team": team_id,
        "user": user_id_2
    }
    }
    response = requests.patch(f'http://127.0.0.1:5000/join_request/{join_request_id}/withdraw/')
    assert response.content == b'Conflict'
    assert response.status_code == 409
    response = requests.patch(f'http://127.0.0.1:5000/join_request/{fake_join_request_id}/withdraw/')
    assert response.content == b'Not Found'
    assert response.status_code == 404
