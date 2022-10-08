import pytest
from Backend import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_create_project(client):
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
    response = client.post('/project/', json={
        "creator": id
    })
    assert response.json
    assert response.status_code == 201
    id = '__________'
    response = client.post('/project/', json={
        "creator": id
    })
    assert response.data == 'Not Found'
    assert response.status_code == 404


def test_get_project(client):
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
    user_id = response.data
    response = client.post('/project/', json={
        "creator": user_id
    })
    project_id = response.data
    assert response.status_code == 200
    response = client.get(f'/project/{project_id}/')
    assert response.data == {
        "project": {
            "id": id,
            "teams": [],
            "users": [user_id],
            "about": {
                "name": "",
                "description": "",
            }
        }
    }
    assert response.status_code == 200
    project_id = '__________'
    response = client.get(f'/project/{project_id}/')
    assert response.data == f'Not Found'
    assert response.status_code == 404


def test_project_add_users(client):
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
    user_id_1 = response.data
    response = client.post('/user/', json={
        "username": "johnny",
        "password": "12345",
        "about": {
            "name": "johnny",
            "email": "johnny@johnny.johnny",
            "phone": "555-5556",
            "bio": "my name is johnny!!!",
        }
    })
    user_id_2 = response.data
    project_id = '__________'
    response = client.patch(f'/project/{project_id}/users/add/', json={
        "user_id": user_id_2
    })
    assert response.data == f'Not Found'
    assert response.status_code == 404
    response = client.post('/project', json={
        "creator": user_id_1
    })
    project_id = response.data
    assert response.status_code == 200
    user_id_3 = '__________'
    response = client.patch(f'/project/{project_id}/users/add/', json={
        "user_id": user_id_3
    })
    assert response.data == f'Not Found'
    assert response.status_code == 404
    response = client.patch(f'/project/{project_id}/users/add/', json={
        "user_id": user_id_2
    })
    assert response.data
    assert response.status_code == 200
    response = client.get(f'/project/{project_id}/')
    assert response.data == {
        "project": {
            "id": id,
            "teams": [],
            "users": [user_id_1, user_id_2],
            "about": {
                "name": "",
                "description": "",
            }
        }
    }


def test_project_remove_users(client):
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
    user_id_1 = response.data
    response = client.post('/user/', json={
        "username": "johnny",
        "password": "12345",
        "about": {
            "name": "johnny",
            "email": "johnny@johnny.johnny",
            "phone": "555-5556",
            "bio": "my name is johnny!!!",
        }
    })
    user_id_2 = response.data
    response = client.post('/project/', json={
        "creator": user_id_1
    })
    project_id = response.data
    response = client.patch(f'/project/{project_id}/users/add/', json={
        "user_id": user_id_2
    })
    assert response.data
    assert response.status_code == 200
    response = client.patch(f'/project/{project_id}/users/remove/', json={
        "user_id": user_id_2
    })
    assert response.data
    assert response.status_code == 200
    response = client.get(f'/project/{project_id}/')
    assert response.data == {
        "project": {
            "id": id,
            "teams": [],
            "users": [user_id_1],
            "about": {
                "name": "",
                "description": "",
            }
        }
    }
    user_id_3 = '__________'
    response = client.patch(f'/project/{project_id}/users/remove/', json={
        "user_id": user_id_3
    })
    assert response.data == f'Not Found'
    assert response.status_code == 404
    project_id = '__________'
    response = client.patch(f'/project/{project_id}/users/remove/', json={
        "user_id": user_id_2
    })
    assert response.data == f'Not Found'
    assert response.status_code == 404


def test_patch_project_about(client):
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
    user_id = response.data
    response = client.post('/project/', json={
        "creator": user_id
    })
    project_id = response.data
    assert response.status_code == 200
    response.patch(f'/project/{project_id}/about/', json={
        "name": "project",
        "description": "this is a cool project"
    })
    assert response.data
    assert response.status_code == 200
    response = client.get(f'/project/{id}/')
    assert response.data == {
        "project": {
            "id": project_id,
            "teams": [],
            "users": [user_id],
            "about": {
                "name": "project",
                "description": "this is a cool project",
            }
        }
    }
