from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_homepage():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Sathwik" in response.text

def test_404():
    response = client.get("/does_not_exist")
    assert response.status_code == 404
    assert "Not Found" in response.text


# Run the tests with the following command:
# pytest test_main.py