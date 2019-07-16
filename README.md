# City Explorer - Python Backend

**Author**: Skyler Burger
**Version**: 1.0.0

## Overview
For this project we are recreating the back end of the City Explorer website. City Explorer is a front end display for calls to various APIs to surface interesting data about a city you'd like to visit. In a previous course we composed a backend to communicate with various APIs and send the data to City Explorer's front end for rendering. We are currently recreating that back end with Python 3.7

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->

## Architecture
This project uses a number of modules from the Python Standard Library such as:
- *http* to create a server instance
- *urllib* to parse URLs and query strings
- *requests* to make requests to APIs
- *os* to access environment variables
- *json* to package up data for transmission

We also utilized the python-dotenv to popular the environment with variables from a .env file.

## API
- */location*: a call to the location path with a location query will return formatted JSON data revealing the original query, a formatted query string, and the lat/long for the given location.

## Change Log
07-15-2019 6:20pm
- /location path is functioning and returning formatted JSON data from the Google Geocode API
