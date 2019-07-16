from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs
import os  # Needed to access env variables with os.getenv()
import requests

from dotenv import load_dotenv
load_dotenv()


# =======
# CLASSES
# =======

# LOCATION
# https://maps.googleapis.com/maps/api/geocode/json?address=${this.query}&key=${process.env.GEOCODE_API_KEY}
# self.search_query
# self.formatted_query from formatted_address

class Location:
    """Normalizes Google Geocode API results for City Explorer."""
    def __init__(self, url, query):
        """Initializes a Location object."""
        self.search_query = query
        self.get_location_data(url)

    def get_location_data(self, url):
        result = requests.get(url).json()
        self.formatted_query = result['results'][0]['formatted_address']
        self.latitude = result['results'][0]['geometry']['location']['lat']
        self.longitude = result['results'][0]['geometry']['location']['lng']

    def serialize(self):
        return vars(self)


# WEATHER
# https://api.darksky.net/forecast/${process.env.WEATHER_API_KEY}/${request.query.data.latitude},${request.query.data.longitude}
# self.forecast from day.summary

# ======
# SERVER
# ======
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Break URL into path, query, params, etc
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/location':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers

            # Break out the queries; {'data':['barcelona']}
            parsed_qs = parse_qs(parsed_path.query)
            query = parsed_qs['data'][0]
            GEOCODE_API_KEY = os.getenv('GEOCODE_API_KEY')
            url = f'https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={GEOCODE_API_KEY}'
            location = Location(url, query)

            data = [location.serialize()]
            json_string = json.dumps(data)
            print(json_string)

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
