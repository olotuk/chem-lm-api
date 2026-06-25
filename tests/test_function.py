
from functions import featurize
from pytest import approx
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_uno():
    risultato = featurize("CCO")
    assert risultato["MolWt"] == approx(46, abs=1)

def test_api_nofunctionality():
    response = client.post("/predict", json={"smiles" : "xyz123"})
    assert response.status_code == 422
    assert "detail" in response.json()