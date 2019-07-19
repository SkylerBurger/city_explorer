from app import db

import os
import requests
# https://api.yelp.com/v3/businesses/search?location=${request.query.data.search_query}
# class Yelp(db.Model):
#     pass
    # tableName = 'yelps'
    # name = business.name
    # image_url = business.image_url
    # price = business.price
    # rating = business.rating
    # url = business.url


class Yelp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurants = db.Column(db.Text)

    @staticmethod
    def create_entry(query):
        """
        Takes in a search query.
        Retrieves Yelp API restaurants data.
        Returns a Yelp instance.
        """
        # Generate API URL and headers
        YELP_API_KEY = os.getenv('YELP_API_KEY')
        url = f'https://api.yelp.com/v3/businesses/search?location={query}?limit=10'
        print('********', url)
        # bearer_string = f'Bearer {YELP_API_KEY}'
        headers = {"Authorization": f'Bearer {YELP_API_KEY}'}

        # Request Yelp API data
        api_data = requests.get(url, headers=headers).json()

        print('API DATA', api_data)
