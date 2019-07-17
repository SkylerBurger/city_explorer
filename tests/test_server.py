from back_end.location import Location

import json

import pytest

def test_location_data_formatting():
    with open('tests/location_mock.json') as data:
        mock_location = json.loads(data.read())

    location = Location.get_location_data('fake_self', 'fake_url', mock_location)
    assert location.formatted_query == 'Barcelona, Spain'
