from app import db

import os
from time import strptime, strftime

import requests


class Events(db.Model):
    """
    Models local event data.
    """
    id = db.Column(db.Integer, primary_key=True)
    events = db.Column(db.Text)

    @staticmethod
    def create_entry(query):
        """
        Takes in a formatted search query.
        Retrieves Eventbrite API event data.
        Returns an Events instance.
        """
        # Generate API URL
        EVENTBRITE_API_KEY = os.getenv('EVENTBRITE_API_KEY')
        url = f'https://www.eventbriteapi.com/v3/events/search'
        url += f'?token={EVENTBRITE_API_KEY}&location.address={query}'

        # Request Eventbrite API data
        api_data = requests.get(url).json()
        print('******API URL: ', url)

        return Events.instantiate_events(api_data)

    @staticmethod
    def instantiate_events(api_data):
        events = []
        for event in api_data['events'][:10]:
            link = event['url']
            name = event['name']['text']
            time_string = event['start']['local']
            structured_time = strptime(time_string, '%Y-%m-%dT%H:%M:%S')
            formatted_time = strftime('%A %B %d, %Y', structured_time)
            event_date = formatted_time
            summary = event['summary']
            events.append({
                'link': link,
                'name': name,
                'event_date': event_date,
                'summary': summary
            })

        # Create an Events instance
        return Events(events=events)
