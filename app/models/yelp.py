from app import db

import os
import requests


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
        url = f'https://api.yelp.com/v3/businesses/search'
        url += f'?location={query}&limit=10'
        headers = {"Authorization": f'Bearer {YELP_API_KEY}'}

        # Request Yelp API data
        api_data = requests.get(url, headers=headers).json()
        restaurants = []
        for result in api_data.get('businesses'):
            name = result['name']
            image_url = result['image_url']
            price = result['price']
            rating = result['rating']
            url = result['url']
            restaurants.append({
                'name': name,
                'image_url': image_url,
                'price': price,
                'rating': rating,
                'url': url
            })

        # Create a Yelp instance
        return Yelp(restaurants=restaurants)
