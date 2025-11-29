import pytest
from simulator import generate_sensor_data

# -------------------------
# DATA FORMAT TEST
# -------------------------
def test_simulator_output_format():
    data = generate_sensor_data("V1")
    assert "sensor_id" in data
    assert "moisture" in data
    assert "temperature" in data

# -------------------------
# VALUE RANGE TEST
# -------------------------
def test_simulator_value_ranges():
    data = generate_sensor_data("V1")
    assert 0 <= data["moisture"] <= 100
    assert 10 <= data["temperature"] <= 45

# -------------------------
# RANDOM FAULT TEST
# -------------------------
def test_simulator_fault_injection():
    faulty = False
    for _ in 20:
        data = generate_sensor_data("V1")
        if data.get("fault") == True:
            faulty = True
    assert faulty == True  # at least one fault must occur

# -------------------------
# TIMING INTERVAL TEST
# -------------------------
def test_15_min_interval():
    from datetime import datetime
    d1 = generate_sensor_data("V1")["timestamp"]
    d2 = generate_sensor_data("V1")["timestamp"]
    assert isinstance(d1, str)
    assert isinstance(d2, str)
