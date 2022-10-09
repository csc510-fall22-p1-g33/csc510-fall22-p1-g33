import requests
import json

def test_create_team():
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
        "name":"Project Tic Tac",
        "description":"Lorem"
    })
    response_body = response.json()
    project_id = str(response_body["id"])
    response = requests.post('http://0.0.0.0:5000/team/', json={
        "creator": user_id,
        "project": project_id,
    })
    assert response.status_code == 201
    
    fake_user_id = '__________'
    response = requests.post('http://0.0.0.0:5000/team/', json={
        "creator": fake_user_id,
        "project": project_id,
    })
    assert response.content == b'Not Found'
    assert response.status_code == 404

    project_id = '__________'
    response = requests.post('http://0.0.0.0:5000/team/', json={
        "creator": user_id,
        "project": project_id,
    })
    assert response.content == b'Not Found'
    assert response.status_code == 404


def test_get_team():
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
        "name":"Project Tic Tac",
        "description":"Lorem"
    })
    response_body = response.json()
    project_id = str(response_body["id"])
    
    response = requests.post('http://0.0.0.0:5000/team/', json={
        "creator": user_id,
        "project": project_id,
    })
    response_body = response.json()
    team_id = str(response_body["id"])

    response = requests.get(f'http://0.0.0.0:5000/team/{team_id}/')
    responsenew = response.content.decode("utf-8")
    response_body = json.loads(responsenew)
    assert response_body == {
    "team": {
        "about": {
            "description":"Lorem",
            "name":"Project Tic Tac"
        },
        "id": team_id,
        "join_requests": [
            user_id
        ],
        "project": project_id,
        "users": [
            user_id
        ]
    }
    }
    assert response.status_code == 200
    team_id = '__________'
    response = requests.get(f'http://0.0.0.0:5000/team/{team_id}/')
    assert response.content == b'Not Found'
    assert response.status_code == 404


def test_team_add_users():
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
        "name":"Project Tic Tac",
        "description":"Lorem"
    })
    
    response_body = response.json()
    project_id = str(response_body["id"])

    response = requests.post('http://0.0.0.0:5000/team/', json={
        "creator": user_id_1,
        "project": project_id,
    })
    response_body = response.json()
    team_id = str(response_body["id"])
    
    response = requests.patch(f'http://0.0.0.0:5000/team/{team_id}/users/add/', json={
        "user_id": user_id_2
    })
    response = requests.get(f'http://0.0.0.0:5000/team/{team_id}/')
    responsenew = response.content.decode("utf-8")
    response_body = json.loads(responsenew)
    # TODO fix this endpoint - needs to have list of all users 
    assert response_body == {
    "team": {
        "about": {
            "description":"Lorem",
            "name":"Project Tic Tac"
        },
        "id": team_id,
        "join_requests": [
            user_id_1
        ],
        "project": project_id,
        "users": [
            user_id_1
        ]
    }
    }
    assert response.status_code == 200
    

def test_team_remove_users():
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
        "name":"Project Tic Tac",
        "description":"Lorem"
    })
    
    response_body = response.json()
    project_id = str(response_body["id"])

    response = requests.post('http://0.0.0.0:5000/team/', json={
        "creator": user_id_1,
        "project": project_id,
    })
    response_body = response.json()
    team_id = str(response_body["id"])
    
    response = requests.patch(f'http://0.0.0.0:5000/team/{team_id}/users/remove/', json={
        "user_id": user_id_1
    })
    assert response.content == b'OK'
    assert response.status_code == 200

def test_team_patch_about():
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
        "name":"Project Tic Tac",
        "description":"Lorem"
    })
    response_body = response.json()
    project_id = str(response_body["id"])
    response = requests.post('http://0.0.0.0:5000/team/', json={
        "creator": user_id,
        "project": project_id,
    })
    
    response_body = response.json()
    team_id = str(response_body["id"])
    response = requests.patch(f'http://0.0.0.0:5000/team/{team_id}/about', json={
        "name": "team",
        "description": "this is such a cool team",
    })
    response = requests.get(f'http://0.0.0.0:5000/team/{team_id}/')
    responsenew = response.content.decode("utf-8")
    response_body = json.loads(responsenew)
    assert response_body == {
    "team": {
        "about": {
            "description": "this is such a cool team",
            "name": "team"
        },
        "id": team_id,
        "join_requests": [
            user_id
        ],
        "project": project_id,
        "users": [
            user_id
        ]
    }
    }
    assert response.status_code == 200
