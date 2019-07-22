# City Explorer - Python Backend

**Author**: Skyler Burger
**Version**: 1.5.0

## Overview
For this project I am recreating the back end of the [City Explorer](https://codefellows.github.io/code-301-guide/curriculum/city-explorer-app/front-end/) website with Python 3.7 and Flask. City Explorer is a front end for calls to various APIs to surface interesting data about a city you'd like to visit.

## Getting Started
- Clone this repo to your machine.
- Create a virtual environment from within the top level directory of the repo with `pipenv shell`.
- Install the required dependencies with `pipenv install`.
- Create a .env file within the app directory with the following values:
  - GEOCODE_API_KEY=[\<Your Google API KEY with Geocoding API and Maps Static API enabled>](https://cloud.google.com/maps-platform/)
  - WEATHER_API_KEY=[\<Your Dark Sky API key>](https://darksky.net/dev/account)
  - EVENTBRITE_API_KEY=[\<Your Eventbrite API public token>](https://www.eventbrite.com/account-settings/apps)
  - TRAIL_API_KEY=[\<Your Hiking Project API private key>](https://www.hikingproject.com/data)
  - MOVIE_API_KEY=[\<Your MovieDB API Key>](https://developers.themoviedb.org/3/getting-started/introduction)
  - YELP_API_KEY=[\<Your Yelp API key>](https://www.yelp.com/developers/v3/manage_app)
- Let Flask know where the app is located with `export FLASK_APP=app/__init__.py`.
- Initialize the database with:
  - `flask db init`
  - `flask db migrate`
  - `flask db upgrade`
- Start the app with `flask run`
- Go to the [City Explorer](https://codefellows.github.io/code-301-guide/curriculum/city-explorer-app/front-end/) front end.
- Enter `http://localhost:5000` as the URL for the deployed back end.
- Enter your Google API key.
- Begin discovering local events, trails, and more!


## Architecture
### Frameworks
- [**Flask**](https://palletsprojects.com/p/flask/) to create and run our server

### Python Standard Library:
- [**os**](https://docs.python.org/3/library/os.html) to access environment variables
- [**time**](https://docs.python.org/3/library/time.html) to format date strings from epoch seconds

### Packages
- [**flask-migrate**](https://flask-migrate.readthedocs.io/en/latest/) to assist in upgrading the database when the models are altered
- [**flask-sqlalchemy**](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) an object relational mapper (ORM) to interact with a SQLite database
- [**python-dotenv**](https://pypi.org/project/python-dotenv/) to populate the environment with variables from a .env file
- [**requests**](https://pypi.org/project/requests/) to make requests to APIs

## API
- **/location**: a call to the location path with a location query will return formatted JSON data revealing the original query, a formatted query string, and the lat/long for the given location.
- **/weather**: a call to the weather path with a latitude and longitue will return a list of dicts containing times and summarys for a week-long forecast.
- **/yelp**: a call to the yelp path with a search query will return a list of dicts containing information regarding the first ten restaurant results from the Yelp Fusion API.
- **/events**: a call to the events path with a formatted search query will return a list of dicts containing information regarding the first ten event results from the Eventbrite API.
- **/movies**: a call to the movies path with a search query will return a list of dicts containing information regarding the first 5 movie results from the Movie DB API.
- **/trails**: a call to the trails path with a latitude and longitude will return a list of dicts containing information regarding local trails results from the Hiking Project API.

## Change Log
07-15-2019 - 1.2.0
- /location path is functioning and returning formatted JSON data from the Google Geocode API

07-16-2019 - 1.3.0
- Application has been refactored to use the Flask framework
- /weather path is functioning and returning formatted JSON data from the Dark Sky API

07-17-2019 1.3.1
- Implemented SQLAlchemy to cache location data to reduce calls to the Google Geocode API

07-19-2019 1.4.0
- /yelp path is functioning and returning formatted JSON data from the Yelp API
- /events path is functioning and returning formatted JSON data from the Eventbrite API
- /movies path is functioning and returning formatted JSON data from the MovieDB API
- /trails path is functioning and returning formatted JSON data from the Hiking Project API

07-21-2019 1.5.0
- Testing of all paths completed.
