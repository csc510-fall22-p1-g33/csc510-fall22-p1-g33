import pytest
from Backend import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_create_user(client):
    response = client.post('/user/', json={
        "username": "john",
        "password": "1234",
        "about": {
            "name": "john",
            "email": "john@john.john",
            "phone": "555-5555",
            "bio": "my name is john",
        }
    })
    assert response.data
    assert response.status_code == 201
    response = client.post('/user/', json={
        "username": "john",
        "password": "1234",
        "about": {
            "name": "john",
            "email": "john@john.john",
            "phone": "555-5555",
            "bio": "my name is john",
        }
    })
    assert response.data == 'Conflict: User already exists.'
    assert response.status_code == 409


def test_get_user(client):
    response = client.post('/user/', json={
        "username": "john",
        "password": "1234",
        "about": {
            "name": "john",
            "email": "john@john.john",
            "phone": "555-5555",
            "bio": "my name is john",
        }
    })
    id = response.data
    response = client.get(f'/user/{id}/')
    assert response.data == {
        "username": "john",
        "password": "1234",
        "about": {
            "name": "john",
            "email": "john@john.john",
            "phone": "555-5555",
            "bio": "my name is john",
        }
    }
    assert response.status_code == 200
    response = client.post('/user/', json={
        "username": "john",
        "password": "1234",
        "about": {
            "name": "johnny",
            "email": "johnny@johnny.johnny",
            "phone": "555-5556",
            "bio": "my name is johnny!!!",
        }
    })
    id = response.data
    assert response.status_code == 200
    response = client.get(f'/user/{id}/')
    assert response.data == {
        "username": "john",
        "password": "1234",
        "about": {
            "name": "johnny",
            "email": "johnny@johnny.johnny",
            "phone": "555-5556",
            "bio": "my name is johnny!!!",
        }
    }
    assert response.status_code == 200
    id = '__________'
    response = client.get(f'/user/{id}/')
    assert response.data == 'Not Found'
    assert response.status_code == 404


# def test_delete_user(client):
#     response = client.post('/user', data={
#         "username": "john",
#         "password": "1234",
#         "about": {
#             "name": "john",
#             "email": "john@john.john",
#             "phone": "555-5555",
#             "bio": "my name is john",
#         }
#     })
#     id = response.data
#     assert response.status_code == 200
#     response = client.delete('/user/{id}')
#     assert response.status_code == 200
#     response = client.get('/user/{id}')
#     assert response == 'Not Found'
#     assert response.status_code == 200


def test_edit_user_about(client):
    response = client.post('/user/', json={
        "username": "john",
        "password": "1234",
        "about": {
            "name": "john",
            "email": "john@john.john",
            "phone": "555-5555",
            "bio": "my name is john",
        }
    })
    id = response.data
    assert response.status_code == 200
    response = client.get(f'/user/{id}/')
    assert response.data == {
        "username": "john",
        "password": "1234",
        "about": {
            "name": "john",
            "email": "john@john.john",
            "phone": "555-5555",
            "bio": "my name is john",
        }
    }
    assert response.status_code == 200
    response = client.patch(f'/user/{id}/about/', json={
        "name": "johnny",
        "email": "johnny@johnny.johnny",
        "phone": "555-5556",
        "bio": "my name is johnny!!!",
    })
    response = client.get(f'/user/{id}/')
    assert response.data == {
        "username": "john",
        "password": "1234",
        "about": {
            "name": "johnny",
            "email": "johnny@johnny.johnny",
            "phone": "555-5556",
            "bio": "my name is johnny!!!",
        }
    }
    assert response.status_code == 200
    id = '__________'
    response = client.patch(f'/user/{id}/about/', json={
        "name": "johnny",
        "email": "johnny@johnny.johnny",
        "phone": "555-5556",
        "bio": "my name is johnny!!!",
    })
    assert response.data == 'Not Found'
    assert response.status_code == 404
