class IrrigationEngine:
    def evaluate_zone(self, zone_id, sensor_data, weather_data, crop_data):
        moisture = sensor_data.get("moisture", 50)

        if moisture < 30:
            return {"action": "IRRIGATE_IMMEDIATELY"}
        if moisture > 85:
            return {"action": "BLOCK"}
        if weather_data.get("rain_48h", 0) > 10:
            return {"action": "SKIP"}

        if moisture < 40:
            return {"action": "SCHEDULE"}

        return {"action": "NO_ACTION"}

