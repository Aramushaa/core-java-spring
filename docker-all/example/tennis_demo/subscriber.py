from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleSubscriber(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_length)
        data = json.loads(post_body.decode('utf-8'))

        print("[🎾] Ball movement detected:", data)

        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    server_address = ('', 8083)
    httpd = HTTPServer(server_address, SimpleSubscriber)
    print("[🟢] Listening for ball movement events on port 8083...")
    httpd.serve_forever()
