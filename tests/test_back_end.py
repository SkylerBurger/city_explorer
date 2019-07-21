from app.models.location import Location
from app.models.weather import Weather
from app.models.yelp import Yelp
from app.models.events import Events

import json

import pytest


# ========
# FIXTURES
# ========

@pytest.fixture
def location():
    with open('tests/demo_geocode_data.json') as file_object:
        contents = json.load(file_object)

    return Location.instantiate_location(contents, 'newhalem')


@pytest.fixture
def weather():
    with open('tests/demo_dark_sky_data.json') as file_object:
        contents = json.load(file_object)

    return Weather.instantiate_weather(contents)


@pytest.fixture
def yelp():
    with open('tests/demo_yelp_data.json') as file_object:
        contents = json.load(file_object)

    return Yelp.instantiate_yelp(contents)


@pytest.fixture
def events():
    with open('tests/demo_eventbrite_data.json') as file_object:
        contents = json.load(file_object)

    return Events.instantiate_events(contents)


# =====
# TESTS
# =====

def test_create_location(location):
    assert location.formatted_query == 'Newhalem, WA 98267, USA'
    assert location.search_query == 'newhalem'
    assert location.latitude == 48.673889
    assert location.longitude == -121.246111


def test_location_dict(location):
    location_dict = location.to_dict()

    assert location_dict['search_query'] == 'newhalem'
    assert location_dict['formatted_query'] == 'Newhalem, WA 98267, USA'
    assert location_dict['latitude'] == 48.673889
    assert location_dict['longitude'] == -121.246111


def test_create_weather(weather):
    with open('tests/demo_dailies.json') as file_object:
        contents = json.load(file_object)
    assert weather.dailies == contents


def test_create_yelp(yelp):
    with open('tests/demo_restaurants.json') as file_object:
        contents = json.load(file_object)
    assert yelp.restaurants == contents


def test_create_events(events):
    with open('tests/demo_events.json') as file_object:
        contents = json.load(file_object)
    assert events.events == contents
