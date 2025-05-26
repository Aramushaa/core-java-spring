import requests

# Base URL for the unregister endpoint
REGISTRY_URL = "http://localhost:8443/serviceregistry/unregister"

# Define the parameters as a dictionary, matching the expected query parameter names
params = {
    "service_definition": "room-temperature-sensor",
    "system_name": "room-temp-sensor-1",
    "address": "localhost",
    "port": 8082,
    "service_uri": "/room-temperature-event"
}

try:
    # Use params argument for DELETE requests to send data as query parameters
    response = requests.delete(REGISTRY_URL, params=params)
    if response.ok:
        print("[✅] Publisher unregistration successful:", response.status_code)
    else:
        print(f"[❌] Publisher unregistration failed: {response.status_code} - {response.text}")
except requests.exceptions.RequestException as e:
    print(f"[🚨] Could not reach Service Registry for unregistration: {e}")