import requests

SERVICE_REGISTRY_URL = "http://localhost:8443/serviceregistry/register"

payload = {
    "systemName": "movement-logger",
    "address": "localhost",
    "port": 8083,
    "authenticationInfo": None
}

try:
    response = requests.post(SERVICE_REGISTRY_URL, json=payload)
    if response.ok:
        print("[✅] Subscriber registered successfully.")
    else:
        print(f"[❌] Subscriber registration failed: {response.status_code} - {response.text}")
except Exception as e:
    print("[❌] Exception occurred:", str(e))
