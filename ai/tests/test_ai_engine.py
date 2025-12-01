from rule_engine import IrrigationEngine
from et_calculator import calculate_et0

engine = IrrigationEngine()

sensor_data = {"moisture": 28, "temperature": 24}
weather_data = {"rain_48h": 0, "et0": 4.5}
crop_data = {"stage": "vegetative"}

def test_et_calculator_accuracy():
    et = calculate_et0(25, 60, 2.0, 500, 20)
    assert et > 0
    assert et < 10

def test_critical_moisture_rule():
    result = engine.evaluate_zone(1, {"moisture": 20}, weather_data, crop_data)
    assert result["action"] == "IRRIGATE_IMMEDIATELY"

def test_rain_skip_rule():
    result = engine.evaluate_zone(
        1,
        {"moisture": 45},
        {"rain_48h": 15},
        crop_data
    )
    assert result["action"] == "SKIP"

def test_saturation_block():
    result = engine.evaluate_zone(
        1,
        {"moisture": 90},
        weather_data,
        crop_data
    )
    assert result["action"] == "BLOCK"

def test_normal_irrigation_rule():
    result = engine.evaluate_zone(
        1,
        {"moisture": 35},
        weather_data,
        crop_data
    )
    assert result["action"] in ["SCHEDULE", "NO_ACTION"]

