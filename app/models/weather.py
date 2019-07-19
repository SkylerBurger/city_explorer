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

    def to_dict(self):
        """
        Returns the weather model's attributes within a dictionary.
        """
        return {
            'dailies': self.dailies
        }

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
        result = requests.get(url).json()
        result = result['daily']['data']
        dailies = []
        for day in result:
            date_string = strftime('%A %B %d, %Y', localtime(day['time']))
            dailies.append({'time': date_string, 'forecast': day['summary']})

        # Create a Weather instance
        return Weather(dailies=dailies)
