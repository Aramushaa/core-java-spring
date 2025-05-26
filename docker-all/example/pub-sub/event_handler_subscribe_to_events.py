import requests

EVENTHANDLER_URL = "http://localhost:8455/eventhandler/subscribe"

payload = {
    "eventType": "room-temperature-event",
    "subscriberSystem": {
        "systemName": "subscriber-1",
        "address": "host.docker.internal",
        "port": 8083,
        "authenticationInfo": None,
        "metadata": {}
    },
    "notifyUri": "/room-temperature-event",
    "matchMetaData": False,
    "filterMetaData": {},
    "sources": []  # 👈 Wildcard: accept all
}



try:
    response = requests.post(EVENTHANDLER_URL, json=payload)
    if response.ok:
        print("[✅] Subscription created successfully with EventHandler.")
    else:
        print(f"[❌] Subscription failed: {response.status_code} - {response.text}")
except requests.exceptions.RequestException as e:
    print(f"[🚨] Could not reach EventHandler: {e}")