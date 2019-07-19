from app import db

import os
import requests


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search_query = db.Column(db.String(256), unique=True)
    formatted_query = db.Column(db.String(256))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def to_dict(self):
        return {
            'search_query': self.search_query,
            'formatted_query': self.formatted_query,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

    @staticmethod
    def generate_api_url(query):
        """
        Takes in a request path.
        Formats a URL to request location data from Google's Geocode API.
        Calls a static method of Location to request location data from the API.
        Returns the model returned from get_location_data().
        """
        GEOCODE_API_KEY = os.getenv('GEOCODE_API_KEY')
        url = 'https://maps.googleapis.com/maps/api/geocode/'
        url += f'json?address={query}&key={GEOCODE_API_KEY}'
        return Location.get_location_data(query, url)

    @staticmethod
    def get_location_data(query, url):
        """
        Takes in the original search query and the formatted API URL.
        Requests data from the Google Geocode API.
        Parses information needed to create a Location entry in the database.
        Makes a call to the Location class and returns a Location entry.
        """
        api_data = requests.get(url).json()
        formatted_query = api_data['results'][0]['formatted_address']
        latitude = api_data['results'][0]['geometry']['location']['lat']
        longitude = api_data['results'][0]['geometry']['location']['lng']
        return Location(formatted_query=formatted_query, latitude=latitude, longitude=longitude, search_query=query)








# https://www.eventbriteapi.com/v3/events/search?token=${process.env.EVENTBRITE_API_KEY}&location.address=${request.query.data.formatted_query}
# class Events(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
    # link = event.url
    # name = event.name.text
    # event_date = event.start.local   but only a slice of it
    # summary = event.summary


# https://api.themoviedb.org/3/search/movie/?api_key=${process.env.MOVIE_API_KEY}&language=en-US&page=1&query=${request.query.data.search_query}
# class Movies(db.Model):
#     pass
    # title = movie.title
    # overview = movie.overview
    # average_votes = movie.vote_average
    # total_votes = move.vote_count
    # image_url = 'https://image.tmdb.org/t/p/w500' + movie.poster_path
    # popularity = movie.popularity
    # released_on = movie.release_date


# https://api.yelp.com/v3/businesses/search?location=${request.query.data.search_query}
# class Yelp(db.Model):
#     pass
    # tableName = 'yelps'
    # name = business.name
    # image_url = business.image_url
    # price = business.price
    # rating = business.rating
    # url = business.url


# https://www.hikingproject.com/data/get-trails?lat=${request.query.data.latitude}&lon=${request.query.data.longitude}&maxDistance=200&key=${process.env.TRAIL_API_KEY}
# class Hikes(db.Model):
#     pass
    # name = trail.name
    # location = trail.location
    # length = trail.length
    # stars = trail.stars
    # star_votes = trail.starVotes
    # summary = trail.summary
    # trail_url = trail.url
    # conditions = trail.conditionDetails
    # condition_date = trail.conditionDate.slice(0, 10)
    # condition_time = trail.conditionDate.slice(12)
