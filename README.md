# City Explorer - Python Backend

**Author**: Skyler Burger
**Version**: 1.4.0

## Overview
For this project I am recreating the back end of the [City Explorer](https://codefellows.github.io/code-301-guide/curriculum/city-explorer-app/front-end/) website with Python 3.7 and Flask. City Explorer is a front end for calls to various APIs to surface interesting data about a city you'd like to visit.

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->

## Architecture
### Frameworks
- **Flask** to create and run our server

### Python Standard Library:
- **requests** to make requests to APIs
- **os** to access environment variables
- **time** to format date strings from epoch seconds

### Packages
- **python-dotenv** to populate the environment with variables from a .env file
- **flask-sqlalchemy** an object relational mapper (ORM) to interact with a SQLite database
- **flask-migrate** to assist in upgrading the database when the models are altered

## API
- **/location**: a call to the location path with a location query will return formatted JSON data revealing the original query, a formatted query string, and the lat/long for the given location.
- **/weather**: a call to the weather path with a latitude and longitue will return a list of dicts containing times and summarys for a week-long forecast.
- **/yelp**: a call to the yelp path with a search query will return a list of dicts containing information regarding the first ten restaurant results from the Yelp Fusion API.
- **/events**: a call to the events path with a formatted search query will return a list of dicts containing information regarding the first ten event results from the Eventbrite API.

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
