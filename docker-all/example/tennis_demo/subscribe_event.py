import requests

EVENT_HANDLER_URL = "http://localhost:8455/eventhandler/subscribe"

payload = {
    "eventType": "ball-movement-event",
    "subscriberSystem": {
        "systemName": "movement-logger",
        "address": "localhost",
        "port": 8083,
        "authenticationInfo": None,
        "metadata": {}
    },
    "notifyUri": "/ball-detected",  # باید این URI توی سابسکرایبرت هندل بشه
    "matchMetaData": False,
    "filterMetaData": {},
    "sources": [
        {
            "systemName": "ball-camera",
            "address": "localhost",
            "port": 8081,
            "authenticationInfo": None,
            "metadata": {}
        }
    ]
}

try:
    response = requests.post(EVENT_HANDLER_URL, json=payload)
    if response.ok:
        print("[✅] Subscription created successfully.")
    else:
        print(f"[❌] Subscription failed: {response.status_code} - {response.text}")
except Exception as e:
    print("[❌] Exception occurred:", str(e))
