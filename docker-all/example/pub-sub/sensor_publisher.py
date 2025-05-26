import requests
import json
import time
import random
from datetime import datetime, timezone # Import timezone

PUBLISH_URL = "http://localhost:8455/eventhandler/publish"

while True:
    temp = round(random.uniform(18.0, 26.0), 2)
    sensor_id = "room-temp-sensor-1"

    payload = {
        "eventType": "room-temperature-event",
        "metaData": {
            "unit": "celsius"
        },
        "payload": json.dumps({
            "sensor_id": sensor_id,
            "temperature": temp
        }),
        "source": {
            "systemName": sensor_id,
            "address": "localhost",
            "port": 8082
        },
        # Corrected timestamp format
        "timeStamp": datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')
    }

    try:
        res = requests.post(PUBLISH_URL, json=payload)
        print(f"[📤 SENT] Published {temp}°C | Status: {res.status_code} | Response: {res.text}")
    except Exception as e:
        print("[🚨] Failed to publish:", e)

    time.sleep(10)