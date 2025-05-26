from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class TempRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        print(f"[🔍] Incoming POST at path: {self.path}")
        if self.path != "/room-temperature-event":
            self.send_error(404, "Wrong endpoint.")
            return
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        try:
            # First parse the full event payload
            full_payload = json.loads(post_data)
            raw_sensor_data = full_payload.get("payload")

            # payload is a JSON string — parse again!
            sensor_data = json.loads(raw_sensor_data)

            temperature = sensor_data.get("temperature")
            sensor_id = sensor_data.get("sensor_id")

            print(f"[📥 RECEIVED] Temperature: {temperature}°C from sensor: {sensor_id}")
            self.send_response(200)
        except json.JSONDecodeError:
            print("[❌] Invalid JSON received.")
            self.send_response(400)
        self.end_headers()

    def do_GET(self):
        self.send_error(501, "GET method not supported.")

if __name__ == "__main__":
    # --- IMPORTANT CHANGE HERE ---
    # Your subscriber server runs on the host, so it should bind to 'localhost' or '0.0.0.0'
    # 'host.docker.internal' is for Docker containers to reach the host, not for the host to bind to itself.
    server_address = ("localhost", 8083) # Use "0.0.0.0" if "localhost" doesn't work for some reason
    httpd = HTTPServer(server_address, TempRequestHandler)
    print("[🌐] Subscriber running on http://localhost:8083")
    httpd.serve_forever()