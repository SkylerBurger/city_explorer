import json, os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

from dotenv import load_dotenv
load_dotenv()

from location import Location


# ======
# SERVER
# ======
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/location':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            location = Location(parsed_path)
            json_string = json.dumps(location.serialize())
            print(json_string.encode())

            self.wfile.write(json_string.encode())
            return

        # For invalid paths
        self.send_response_only(404)
        self.end_headers()


# =====================
# SERVER INITIALIZATION
# =====================

def create_server():
    return HTTPServer(
        ('127.0.0.1', 3000), SimpleHandler
    )

def run_forever():
    server = create_server()
    try:
        print(f'Serving on Port: {os.getenv("PORT")}')
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        server.shutdown()

run_forever()
