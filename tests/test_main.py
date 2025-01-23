from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Service is running"}

def test_predict():
    payload = {
        "user_agent": "Mozilla/5.0 (Windows)",
        "tls_ja3": "769,47-53-255,0-23-65281-10-11,29-23",
        "ttl": 128
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "is_anomaly" in response.json()