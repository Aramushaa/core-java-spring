import requests

REGISTRY_URL = "http://localhost:8443/serviceregistry/register"

payload = {
    "serviceDefinition": "room-temp-subscriber",
    "providerSystem": {
        "systemName": "subscriber-1",
        "address": "host.docker.internal",
        "port": 8083
    },
    "serviceUri": "/room-temperature-event",
    "secure": "NOT_SECURE",
    "interfaces": [
        "HTTP-INSECURE-JSON"
    ],
    "metadata": {
        "role": "logger",
        "event_type": "room-temperature-event"
    }
}

response = requests.post(REGISTRY_URL, json=payload)
print("[✅] Subscriber 1 registration:", response.status_code, response.text)