from app import db

import os

import requests


class Movies(db.Model):
    """
    Models the data of movies related to a given location.
    """
    id = db.Column(db.Integer, primary_key=True)
    movies = db.Column(db.Text)

    @staticmethod
    def create_entry(query):
        """
        Takes in a search query.
        Retrieves MovieDB API movie data.
        Returns an Movies instance.
        """
        # Generate API URL
        MOVIE_API_KEY = os.getenv('MOVIE_API_KEY')
        url = 'https://api.themoviedb.org/3/search/movie/'
        url += f'?api_key={MOVIE_API_KEY}&language=en-US&page=1&query={query}'

        # Request MovieDB API data
        api_data = requests.get(url).json()

        return Movies.instantiate_movies(api_data)

    @staticmethod
    def instantiate_movies(api_data):
        movies = []
        for movie in api_data['results'][:5]:
            title = movie['title']
            overview = movie['overview']
            average_votes = movie['vote_average']
            total_votes = movie['vote_count']
            image_url = 'https://image.tmdb.org/t/p/w500' + movie['poster_path']
            popularity = movie['popularity']
            released_on = movie['release_date']
            movies.append({
                'title': title,
                'overview': overview,
                'average_votes': average_votes,
                'total_votes': total_votes,
                'image_url': image_url,
                'popularity': popularity,
                'released_on': released_on
            })

        # Create a Movies instance
        return Movies(movies=movies)
