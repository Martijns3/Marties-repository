import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_redirect(client):
    response = client.get("/home")
    assert response.status_code == 302
    assert response.location == "http://localhost:5000/"


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<title>Index</title>" in response.data


def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"<title>About</title>" in response.data


""" Write your own tests below."""

def test_contact(client):
    response = client.get("/contact")
    assert response.status_code == 200
    assert b"<title>Contact</title>" in response.data