from app import db

import os
import requests
from time import localtime, strftime


class Weather(db.Model):
    """
    Models a weekly weather forecast.
    """
    id = db.Column(db.Integer, primary_key=True)
    dailies = db.Column(db.Text)

    @staticmethod
    def create_entry(lat, long):
        """
        Takes in the latitude and longitude of a location.
        Retrieves weather data from the Dark Sky API.
        Returns a Weather instance.
        """
        # Generate API URL
        WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
        url = 'https://api.darksky.net/forecast/'
        url += f'{WEATHER_API_KEY}/{lat},{long}'

        # Request Dark Sky API data
        api_data = requests.get(url).json()
        api_data = api_data['daily']['data']

        return Weather.instantiate_weather(api_data)

    @staticmethod
    def instantiate_weather(api_data):
        dailies = []
        for day in api_data:
            date_string = strftime('%A %B %d, %Y', localtime(day['time']))
            dailies.append({'time': date_string,
                            'forecast': day['summary']})

        # Create a Weather instance
        return Weather(dailies=dailies)
