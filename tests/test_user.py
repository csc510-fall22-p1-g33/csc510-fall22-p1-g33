import requests
import json

def test_create_user():
    response = requests.post('http://0.0.0.0:5000/user/', json={
        "username": "john1",
        "password": "1234",
        "about": {
            "name": "john",
            "email": "john@john.john",
            "phone": "555-5555",
            "bio": "my name is john",
        }
    })
    response_body = response.json()
    assert response_body
    assert response.status_code == 201
    response = requests.post('http://0.0.0.0:5000/user/', json={
        "username": "john1",
        "password": "1234",
        "about": {
            "name": "john",
            "email": "john@john.john",
            "phone": "555-5555",
            "bio": "my name is john",
        }
    })
    assert response.content == b'Conflict: User already exists.'
    assert response.status_code == 409


def test_get_user():
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
    id = response_body["id"]
    
    response = requests.get(f'http://0.0.0.0:5000/user/{id}/')
    responsenew = response.content.decode("utf-8")
    response_body = json.loads(responsenew)
    assert response_body == {
        "user": {
            "about": {
                "name": "john",
                "email": "john@john.john",
                "phone": "555-5555",
                "bio": "my name is john",
            },
            "id": "1",
            "join_requests": [],
            "password": "1234",
            "projects": [],
            "teams": [],
            "username": "john",
        }
    }
    assert response.status_code == 200
    id = '__________'
    response = requests.get(f'http://0.0.0.0:5000/user/{id}/')
    assert response.content == b'Not Found'
    assert response.status_code == 404

def test_edit_user_about():
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
    id = response_body["id"]
    assert response.status_code == 201

    response = requests.patch(f'http://0.0.0.0:5000/user/{id}/about/', json={
    "about": {
        "name": "John",
        "email": "jdoe@ncsu.edu",
        "phone": "9999999999",
        "bio": "I'm not cool."
    }
    })

    response = requests.get(f'http://0.0.0.0:5000/user/{id}/')
    responsenew = response.content.decode("utf-8")
    response_body = json.loads(responsenew)
    assert response_body == {
    "user": {
            "about": {
                "name": "John",
                "email": "jdoe@ncsu.edu",
                "phone": "9999999999",
                "bio": "I'm not cool."
            },
            "id": str(id),
            "join_requests": [],
            "password": "1234",
            "projects": [],
            "teams": [],
            "username": "john",
        }
    }
    assert response.status_code == 200

# TODO implement after the route is up
# def test_delete_user(client):
#     response = requests.post('http://0.0.0.0:5000/user', data={
#         "username": "john",
#         "password": "1234",
#         "about": {
#             "name": "john",
#             "email": "john@john.john",
#             "phone": "555-5555",
#             "bio": "my name is john",
#         }
#     })
#     id = response["content"]
#     assert response.status_code == 200
#     response = requests.delete('http://0.0.0.0:5000/user/{id}')
#     assert response.status_code == 200
#     response = requests.get('http://0.0.0.0:5000/user/{id}')
#     assert response == 'Not Found'
#     assert response.status_code == 200