from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_ram_info():
    response = client.get("/ram_info/1")
    assert response.status_code == 200
    data = response.json()
    assert len(data[0]) == 3
