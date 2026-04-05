from fastapi.testclient import TestClient
from app import app

# Create a test client to simulate HTTP requests without starting a real server
client = TestClient(app)

def test_read_main():
    # TEST: Ensure the homepage loads with a 200 OK status
    response = client.get("/")
    assert response.status_code == 200
    assert "Online" in response.text

def test_health():
    # TEST: Ensure the API health endpoint returns the correct JSON
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}