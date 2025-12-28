import time

def ingest_sensor(sensor_id, value):
    return {
        "type": "sensor",
        "sensor_id": sensor_id,
        "value": value,
        "location": "Hyderabad",
        "timestamp": time.time()
    }
