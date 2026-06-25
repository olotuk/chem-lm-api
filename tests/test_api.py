from fastapi.testclient import TestClient
from app.main import app



client = TestClient(app)

def test_api_functionality():
    response = client.post("/predict", json={"smiles" : "CCO"})
    assert response.status_code == 200
    assert "prediction" in response.json()
