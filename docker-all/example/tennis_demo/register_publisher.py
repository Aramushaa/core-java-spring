import requests

SERVICE_REGISTRY_URL = "http://localhost:8443/serviceregistry/register"

payload = {
    "systemName": "ball-camera",
    "address": "localhost",
    "port": 8081,
    "authenticationInfo": None
}

try:
    response = requests.post(SERVICE_REGISTRY_URL, json=payload)
    if response.ok:
        print("[✅] Publisher registered successfully.")
    else:
        print(f"[❌] Publisher registration failed: {response.status_code} - {response.text}")
except Exception as e:
    print("[❌] Exception occurred:", str(e))
