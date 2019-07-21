from app.models.location import Location

import json

import pytest


@pytest.fixture
def location():
    with open('tests/demo_geocode_data.json') as file_object:
        contents = json.load(file_object)

    return Location.instantiate_location(contents, 'newhalem')


def test_create_location(location):
    assert location.formatted_query == 'Newhalem, WA 98267, USA'


def test_location_dict(location):
    location_dict = location.to_dict()

    assert location_dict['search_query'] == 'newhalem'
    assert location_dict['formatted_query'] == 'Newhalem, WA 98267, USA'
    assert location_dict['latitude'] == 48.673889
    assert location_dict['longitude'] == -121.246111
