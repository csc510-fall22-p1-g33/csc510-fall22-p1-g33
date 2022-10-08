import pytest
from Backend import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_create_join_request(client):
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
    response = client.post('/join_request/', json={
        "creator": user_id_2,
        "team": team_id
    })
    assert response.data
    assert response.status_code == 200
    fake_team_id = '__________'
    fake_user_id = '__________'
    response = client.post('/join_request/', json={
        "creator": user_id_2,
        "team": fake_team_id
    })
    assert response.data == 'Not Found'
    assert response.status_code == 404
    response = client.post('/join_request/', json={
        "creator": fake_user_id,
        "team": team_id,
    })
    assert response.data == 'Not Found'
    assert response.status_code == 404


def test_get_join_request(client):
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
    response = client.post('/join_request/', json={
        "creator": user_id_2,
        "team": team_id
    })
    join_request_id = response.data
    fake_join_request_id = '__________'
    response = client.get(f'/join_request/{join_request_id}/')
    assert response.data == {
        "id": join_request_id,
        "user": user_id_2,
        "team": team_id,
        "status": "pending"
    }
    assert response.status_code == 200
    response = client.get(f'/join_request/{fake_join_request_id}/')
    assert response.data == f'Not Found'
    assert response.status_code == 404


def test_accept_join_request(client):
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
    response = client.post('/join_request/', json={
        "creator": user_id_2,
        "team": team_id
    })
    join_request_id = response.data
    fake_join_request_id = '__________'
    response = client.patch(f'/join_request/{join_request_id}/accept/')
    assert response.data
    assert response.status_code == 200
    response = client.get(f'/join_request/{join_request_id}/')
    assert response.data == {
        "id": join_request_id,
        "user": user_id_2,
        "team": team_id,
        "status": "accepted"
    }
    response = client.patch(f'/join_request/{join_request_id}/accept/')
    assert response.data == 'Conflict'
    assert response.status_code == 409
    response = client.patch(f'/join_request/{fake_join_request_id}/accept/')
    assert response.data == 'Not Found'
    assert response.status_code == 404


def test_reject_join_request(client):
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
    response = client.post('/join_request/', json={
        "creator": user_id_2,
        "team": team_id
    })
    join_request_id = response.data
    fake_join_request_id = '__________'
    response = client.patch(f'/join_request/{join_request_id}/reject/')
    assert response.data
    assert response.status_code == 200
    response = client.get(f'/join_request/{join_request_id}/')
    assert response.data == {
        "id": join_request_id,
        "user": user_id_2,
        "team": team_id,
        "status": "rejected"
    }
    response = client.patch(f'/join_request/{join_request_id}/reject/')
    assert response.data == 'Conflict'
    assert response.status_code == 409
    response = client.patch(f'/join_request/{fake_join_request_id}/reject/')
    assert response.data == 'Not Found'
    assert response.status_code == 404


def test_withdraw_join_request(client):
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
    response = client.post('/join_request/', json={
        "creator": user_id_2,
        "team": team_id
    })
    join_request_id = response.data
    fake_join_request_id = '__________'
    response = client.patch(f'/join_request/{join_request_id}/withdraw/')
    assert response.data
    assert response.status_code == 200
    response = client.get(f'/join_request/{join_request_id}/')
    assert response.data == {
        "id": join_request_id,
        "user": user_id_2,
        "team": team_id,
        "status": "withdrawn"
    }
    response = client.patch(f'/join_request/{join_request_id}/withdraw/')
    assert response.data == 'Conflict'
    assert response.status_code == 409
    response = client.patch(f'/join_request/{fake_join_request_id}/withdraw/')
    assert response.data == 'Not Found'
    assert response.status_code == 404
