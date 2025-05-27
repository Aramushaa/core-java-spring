import requests
import json
import time

EVENTHANDLER_URL = "http://localhost:8455/eventhandler/publish"

event_payload = {
    "eventType": "ball-move-event",
    "source": {
        "systemName": "tennis-camera",
        "address": "localhost",
        "port": 8080
    },
    "payload": json.dumps({"ball_position": [3.2, 7.1], "speed": 42}),
    "metadata": {}
}

print("[📡] Publishing ball movement event...")
response = requests.post(EVENTHANDLER_URL, json=event_payload)
if response.ok:
    print("[✅] Event published.")
else:
    print(f"[❌] Failed to publish event: {response.status_code} - {response.text}")
