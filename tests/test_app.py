from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_ram_info():
    response = client.get("/ram_info/1")
    assert response.status_code == 200
    data = response.json()
    assert 'total' in data[0]
    assert 'free' in data[0]
    assert 'used' in data[0]
