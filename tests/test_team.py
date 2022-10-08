import pytest
from Backend import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_create_team(client):
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
    response = client.post('/team/', json={
        "creator": user_id,
        "project": project_id,
    })
    assert response.data
    assert response.status_code == 201
    fake_user_id = '__________'
    response = client.post('/team/', json={
        "creator": fake_user_id,
        "project": project_id,
    })
    assert response.data == 'Not Found'
    assert response.status_code == 404
    project_id = '__________'
    response = client.post('/team/', json={
        "creator": user_id,
        "project": project_id,
    })
    assert response.data == 'Not Found'
    assert response.status_code == 404


def test_get_team(client):
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
    response = client.post('/team/', json={
        "creator": user_id,
        "project": project_id,
    })
    team_id = response.data
    response = client.get(f'/team/{team_id}/')
    assert response.data == {
        "id": team_id,
        "users": [user_id],
        "join_requests": [],
        "project": [project_id],
        "about": {
            "name": "",
            "description": "",
        },
    }
    assert response.status_code == 200
    team_id = '__________'
    response = client.get(f'/team/{team_id}/')
    assert response.data == 'Not Found'
    response.status_code == 404


def test_team_add_users(client):
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
    response = client.post('/team/', json={
        "creator": user_id_1,
        "project": project_id,
    })
    team_id = response.data
    response = client.patch(f'/team/{team_id}/users/add/', json={
        "user_id": user_id_2
    })
    response = client.get(f'/team/{team_id}/')
    assert response.data == {
        "id": team_id,
        "users": [user_id_1, user_id_2],
        "join_requests": [],
        "project": [project_id],
        "about": {
            "name": "",
            "description": "",
        },
    }
    fake_team_id = '__________'
    fake_user_id = '__________'
    response = client.patch(f'/team/{fake_team_id}/users/add/', json={
        "user_id": user_id_2
    })
    assert response.data == f'Not Found'
    assert response.status_code == 404
    response = client.patch(f'/team/{team_id}/users/add/', json={
        "user_id": fake_user_id
    })
    assert response.data == f'Not Found'
    assert response.status_code == 404


def test_team_remove_users(client):
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
    response = client.post('/team/', json={
        "creator": user_id_1,
        "project": project_id,
    })
    team_id = response.data
    response = client.patch(f'/team/{team_id}/users/add/', json={
        "user_id": user_id_2
    })
    assert response.status_code == 200
    response = client.patch(f'/team/{team_id}/users/remove/', json={
        "user_id": user_id_2
    })
    assert response.status_code == 200
    response = client.get(f'/team/{team_id}/')
    assert response.data == {
        "id": team_id,
        "users": [user_id_1],
        "join_requests": [],
        "project": [project_id],
        "about": {
            "name": "",
            "description": "",
        },
    }
    assert response.status_code == 200
    fake_team_id = '__________'
    fake_user_id = '__________'
    response = client.patch(f'/team/{fake_team_id}/users/remove/', json={
        "user_id": user_id_2
    })
    assert response.data == f'Not Found'
    assert response.status_code == 404
    response = client.patch(f'/team/{team_id}/users/remove/', json={
        "user_id": fake_user_id
    })
    assert response.data == f'Not Found'
    assert response.status_code == 404
    response = client.patch(f'/team/{team_id}/users/remove/', json={
        "user_id": user_id_2
    })
    assert response.data == f'Not Found'
    assert response.status_code == 404


def test_team_patch_about(client):
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
    response = client.post('/team/', json={
        "creator": user_id,
        "project": project_id,
    })
    team_id = response.data
    response = client.patch(f'/team/{team_id}/about', json={
        "name": "team",
        "description": "this is such a cool team",
    })
    response = client.get(f'/team/{team_id}/')
    assert response.data == {
        "id": team_id,
        "users": [user_id],
        "join_requests": [],
        "project": [project_id],
        "about": {
            "name": "team",
            "description": "this is such a cool team",
        },
    }
    assert response.status_code == 200
