from app import db

import os
from time import strptime, strftime

import requests


class Trails(db.Model):
    """
    Models local trail data.
    """
    id = db.Column(db.Integer, primary_key=True)
    trails = db.Column(db.Text)

    @staticmethod
    def create_entry(lat, long):
        """
        Takes in a latitude and longitude.
        Retrieves Hiking Project API trail data.
        Returns a Trails instance.
        """
        # Generate API URL
        TRAIL_API_KEY = os.getenv('TRAIL_API_KEY')
        url = 'https://www.hikingproject.com/data/get-trails'
        url += f'?lat={lat}&lon={long}&maxDistance=200&key={TRAIL_API_KEY}'

        # Request Hiking Project API data
        api_data = requests.get(url).json()
        trails = []
        for trail in api_data['trails'][:5]:
            name = trail.get('name')
            location = trail.get('location')
            length = trail.get('length')
            stars = trail.get('stars')
            star_votes = trail.get('starVotes')
            summary = trail.get('summary')
            trail_url = trail.get('url')
            conditions = trail.get('conditionDetails')
            time_string = trail.get('conditionDate')
            structured_time = strptime(time_string, '%Y-%m-%d %H:%M:%S')
            condition_date = strftime('%A %B %d, %Y', structured_time)
            condition_time = strftime('%H:%M%p', structured_time)
            trails.append({
                'name': name,
                'location': location,
                'length': length,
                'stars': stars,
                'star_votes': star_votes,
                'summary': summary,
                'trail_url': trail_url,
                'conditions': conditions,
                'condition_date': condition_date,
                'condition_time': condition_time
            })

        # Create a Trails instance
        return Trails(trails=trails)
