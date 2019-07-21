from app import db

import os

import requests


class Location(db.Model):
    """
    Models basic location data for use in requests to location-based APIs.
    """
    id = db.Column(db.Integer, primary_key=True)
    search_query = db.Column(db.String(256), unique=True)
    formatted_query = db.Column(db.String(256))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def to_dict(self):
        """
        Returns the location model's attributes within a dictionary.
        """
        return {
            'search_query': self.search_query,
            'formatted_query': self.formatted_query,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

    @staticmethod
    def create_entry(query):
        """
        Takes in a search query.
        Retrieves Google Geocode API location data.
        Returns a Location instance.
        """
        # Generate API URL
        GEOCODE_API_KEY = os.getenv('GEOCODE_API_KEY')
        url = 'https://maps.googleapis.com/maps/api/geocode/'
        url += f'json?address={query}&key={GEOCODE_API_KEY}'

        # Request Geocode API data
        api_data = requests.get(url).json()
        return Location.instantiate_location(api_data, query)

    @staticmethod
    def instantiate_location(api_data, query):
        """
        Takes in Google Geocoding API results and original search query.
        Returns a Location object.
        """
        # Single out the information needed
        formatted_query = api_data['results'][0]['formatted_address']
        latitude = api_data['results'][0]['geometry']['location']['lat']
        longitude = api_data['results'][0]['geometry']['location']['lng']

        # Create a Location instance
        return Location(formatted_query=formatted_query,
                        latitude=latitude,
                        longitude=longitude,
                        search_query=query)
