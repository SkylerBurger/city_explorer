import requests
import os


# WEATHER
# https://api.darksky.net/forecast/${process.env.WEATHER_API_KEY}/${request.query.data.latitude},${request.query.data.longitude}
# a list of dicts containing forecast and time keys.
# time format: Monday July 15, 2019
class Weather:
    def __init__(self, lat, long):
        self.generate_api_url(lat, long)

    def generate_api_url(self, lat, long):
        WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
        url = 'https://api.darksky.net/forecast/'
        url += f'{WEATHER_API_KEY}/{lat},{long}'
        self.get_weather_data(url)

    def get_weather_data(self, url):
        