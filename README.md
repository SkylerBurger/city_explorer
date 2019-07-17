# City Explorer - Python Backend

**Author**: Skyler Burger
**Version**: 1.2.0

## Overview
For this project I am recreating the back end of the City Explorer website with Python 3.7 and Flask. City Explorer is a front end for calls to various APIs to surface interesting data about a city you'd like to visit. In a previous course I composed a backend to communicate with various APIs and send the data to City Explorer's front end for rendering.

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
- **python-dotenv** to populate the environment with variables from a .env file.

## API
- **/location**: a call to the location path with a location query will return formatted JSON data revealing the original query, a formatted query string, and the lat/long for the given location.
- **/weather**: a call to the weather path with a latitude and longitue will return a list of dicts containing times and summarys for a week-long forecast.

## Change Log
07-15-2019 6:20pm
- /location path is functioning and returning formatted JSON data from the Google Geocode API

07-16-2019 5:00pm
- Application has been refactored to use the Flask framework
- /weather path is functioning and returning formatted JSON data from the Dark Sky API
