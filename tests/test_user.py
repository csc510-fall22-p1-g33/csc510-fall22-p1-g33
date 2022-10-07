import pytest
from Backend import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_create_user(client):
    result = client.get('/')
    assert b"Hello world!" in result.data
    response = client.post("/user", data={
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
    response = client.get(f'/user/${id}')
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
