import requests
import os
from time import localtime, strftime


# WEATHER
# URL for localhost testing:
# http://localhost:5000/weather?data%5Bformatted_query%5D=Barcelona%2C%20Spain&data%5Blatitude%5D=41.3850639&data%5Blongitude%5D=2.1734035&data%5Bsearch_query%5D=barcelona
class Weather:
    def __init__(self, lat, long):
        self.generate_api_url(lat, long)

    def generate_api_url(self, lat, long):
        WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
        url = 'https://api.darksky.net/forecast/'
        url += f'{WEATHER_API_KEY}/{lat},{long}'
        print(url)
        self.get_weather_data(url)

    def get_weather_data(self, url):
        result = requests.get(url).json()
        result = result['daily']['data']
        results = []
        for day in result:
            _time = strftime('%A %B %d, %Y', localtime(day['time']))
            results.append({'time': _time, 'forecast': day['summary']})
        self.forecast = results
