import requests
import json


def test_create_project():
    response = requests.post('http://0.0.0.0:5000/user/', json={
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
    id = str(response_body["id"])

    response = requests.post('http://0.0.0.0:5000/project/', json={
        "creator": id,
        "name": "Project Tic Tac",
        "description": "Lorem"
    })
    assert response.status_code == 201

    id = '__________'
    response = requests.post('http://0.0.0.0:5000/project/', json={
        "creator": id,
        "name": "Project Tic Tac",
        "description": "Lorem"
    })

    assert response.content == b'Not Found'
    assert response.status_code == 404


def test_get_project():
    response = requests.post('http://0.0.0.0:5000/user/', json={
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
    user_id = str(response_body["id"])

    response = requests.post('http://0.0.0.0:5000/project/', json={
        "creator": user_id,
        "name": "Project Tic Tac",
        "description": "Lorem"
    })
    response_body = response.json()
    project_id = str(response_body["id"])
    assert response.status_code == 201

    response = requests.get(f'http://0.0.0.0:5000/project/{project_id}/')
    responsenew = response.content.decode("utf-8")
    response_body = json.loads(responsenew)
    assert response_body == {
        "project": {
            "about": {
                "description": "Lorem",
                "name": "Project Tic Tac"
            },
            "id": project_id,
            "teams": [],
            "users": [
                user_id
            ]
        }
    }
    assert response.status_code == 200

    project_id = '__________'
    response = requests.get(f'http://0.0.0.0:5000/project/{project_id}/')
    assert response.content == b'Not Found'
    assert response.status_code == 404


def test_project_add_users():
    response = requests.post('http://0.0.0.0:5000/user/', json={
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
    response = requests.post('http://0.0.0.0:5000/user/', json={
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

    project_id = '__________'
    response = requests.patch(f'http://0.0.0.0:5000/project/{project_id}/users/add/', json={
        "user_id": user_id_2
    })

    assert response.content == b'Not Found'
    assert response.status_code == 404

    response = requests.post('http://0.0.0.0:5000/project', json={
        "creator": user_id_1,
        "description": "Lorem",
        "name": "Project Tic Tac"
    })

    response_body = response.json()
    project_id = str(response_body["id"])
    assert response.status_code == 201

    user_id_3 = '__________'
    response = requests.patch(f'http://0.0.0.0:5000/project/{project_id}/users/add/', json={
        "user_id": user_id_3
    })
    assert response.content == b'Not Found'
    assert response.status_code == 404

    response = requests.patch(f'http://0.0.0.0:5000/project/{project_id}/users/add/', json={
        "user_id": user_id_2
    })
    assert response.status_code == 200

    response = requests.get(f'http://0.0.0.0:5000/project/{project_id}/')
    responsenew = response.content.decode("utf-8")
    response_body = json.loads(responsenew)
    assert response_body == {
        "project": {
            "about": {
                "description": "Lorem",
                "name": "Project Tic Tac"
            },
            "id": project_id,
            "teams": [],
            "users": [
                user_id_1, user_id_2
            ]
        }
    }


def test_project_remove_users():
    response = requests.post('http://0.0.0.0:5000/user/', json={
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

    response = requests.post('http://0.0.0.0:5000/user/', json={
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

    response = requests.post('http://0.0.0.0:5000/project/', json={
        "creator": user_id_1,
        "name": "Project Tic Tac",
        "description": "Lorem"
    })
    response_body = response.json()
    project_id = str(response_body["id"])

    response = requests.patch(f'http://0.0.0.0:5000/project/{project_id}/users/add/', json={
        "user_id": user_id_2
    })
    assert response.status_code == 200

    response = requests.patch(f'http://0.0.0.0:5000/project/{project_id}/users/remove/', json={
        "user_id": user_id_2
    })
    assert response.status_code == 200

    response = requests.get(f'http://0.0.0.0:5000/project/{project_id}/')
    responsenew = response.content.decode("utf-8")
    response_body = json.loads(responsenew)
    assert response_body == {
        "project": {
            "about": {
                "description": "Lorem",
                "name": "Project Tic Tac"
            },
            "id": project_id,
            "teams": [],
            "users": [
                user_id_1
            ]
        }
    }

    user_id_3 = '__________'
    response = requests.patch(f'http://0.0.0.0:5000/project/{project_id}/users/remove/', json={
        "user_id": user_id_3
    })
    assert response.content == b'Not Found'
    assert response.status_code == 404
    project_id = '__________'
    response = requests.patch(f'http://0.0.0.0:5000/project/{project_id}/users/remove/', json={
        "user_id": user_id_2
    })
    assert response.content == b'Not Found'
    assert response.status_code == 404


def test_patch_project_about():
    response = requests.post('http://0.0.0.0:5000/user/', json={
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
    user_id = str(response_body["id"])
    response = requests.post('http://0.0.0.0:5000/project/', json={
        "creator": user_id,
        "name": "Project Tic Tac",
        "description": "Lorem"
    })
    response_body = response.json()
    project_id = str(response_body["id"])
    assert response.status_code == 201
    response = requests.patch(f'http://0.0.0.0:5000/project/{project_id}/about/', json={
        "name": "project",
        "description": "this is a cool project"
    })
    assert response.status_code == 200
    response = requests.get(f'http://0.0.0.0:5000/project/{project_id}/')
    responsenew = response.content.decode("utf-8")
    response_body = json.loads(responsenew)
    assert response_body == {
        "project": {
            "about": {
                "description": "this is a cool project",
                "name": "project"
            },
            "id": project_id,
            "teams": [],
            "users": [
                user_id
            ]
        }
    }
