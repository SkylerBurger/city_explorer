import requests
import os


class LocationNormalizer:
    """Normalizes Google Geocode API results for City Explorer."""
    def __init__(self, query):
        """Initializes a Location object."""
        self.search_query = query
        self.formatted_query = ''
        self.longitude = ''
        self.latitude = ''
        self.generate_api_url(query)

    def generate_api_url(self, query):
        """
        Takes in a request path.
        Formats a URL to request location data from Google's Geocode API.
        """
        GEOCODE_API_KEY = os.getenv('GEOCODE_API_KEY')
        url = 'https://maps.googleapis.com/maps/api/geocode/'
        url += f'json?address={query}&key={GEOCODE_API_KEY}'
        self.get_location_data(url)

    def get_location_data(self, url, result=''):
        if result == '':
            result = requests.get(url).json()
        self.formatted_query = result['results'][0]['formatted_address']
        self.latitude = result['results'][0]['geometry']['location']['lat']
        self.longitude = result['results'][0]['geometry']['location']['lng']

    def serialize(self):
        return vars(self)
