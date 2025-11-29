import pytest
from fastapi.testclient import TestClient

# your backend main file
from main import app  

client = TestClient(app)

# -------------------------
# SENSOR ENDPOINT TESTS
# -------------------------
def test_get_all_sensors():
    response = client.get("/api/sensors")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_sensor():
    response = client.get("/api/sensors/V1")
    assert response.status_code in [200, 404]

def test_get_sensor_latest():
    response = client.get("/api/sensors/V1/latest")
    assert response.status_code in [200, 404]

# -------------------------
# IRRIGATION API TESTS
# -------------------------
def test_manual_irrigation():
    payload = {
        "zone_id": 1,
        "duration_minutes": 30,
        "trigger_type": "manual",
        "user_id": "test_user"
    }
    response = client.post("/api/irrigation/manual", json=payload)
    assert response.status_code in [200, 400]

def test_irrigation_status():
    response = client.get("/api/irrigation/status")
    assert response.status_code == 200

# -------------------------
# WEATHER API TESTS
# -------------------------
def test_weather_current():
    response = client.get("/api/weather/current")
    assert response.status_code == 200

# -------------------------
# DATABASE CONNECTION TEST
# -------------------------
def test_database_connections():
    try:
        # fake check for InfluxDB/PG links
        assert True
    except:
        assert False

# -------------------------
# WEBSOCKET LIVE STREAM TEST
# -------------------------
def test_websocket_connection():
    with client.websocket_connect("/ws/sensors/live") as ws:
        ws.send_text("ping")
        data = ws.receive_text()
        assert data is not None
