import requests, os
from urllib.parse import parse_qs

from dotenv import load_dotenv
load_dotenv()


class Location:
    """Normalizes Google Geocode API results for City Explorer."""
    def __init__(self, parsed_path):
        """Initializes a Location object."""
        self.search_query = ''
        self.formatted_query = ''
        self.longitude = ''
        self.latitude = ''
        self.generate_api_url(parsed_path)

    def get_location_data(self, url):
        result = requests.get(url).json()
        self.formatted_query = result['results'][0]['formatted_address']
        self.latitude = result['results'][0]['geometry']['location']['lat']
        self.longitude = result['results'][0]['geometry']['location']['lng']

    def generate_api_url(self, parsed_path):
        """Takes in a request path and formats a URL to request location data from Google's Geocode API."""
        # Break out the queries; {'data':['barcelona']}
        parsed_qs = parse_qs(parsed_path.query)
        self.search_query = parsed_qs['data'][0]
        GEOCODE_API_KEY = os.getenv('GEOCODE_API_KEY')
        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={self.search_query}&key={GEOCODE_API_KEY}'
        self.get_location_data(url)

    def serialize(self):
        return vars(self)

# WEATHER
# https://api.darksky.net/forecast/${process.env.WEATHER_API_KEY}/${request.query.data.latitude},${request.query.data.longitude}
# self.forecast from day.summary
