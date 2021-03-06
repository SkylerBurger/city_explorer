from config import Config

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from dotenv import load_dotenv
load_dotenv()


# ===
# APP
# ===
app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# ======
# ROUTES
# ======
@app.route('/location')
def location_route():
    query = request.args.get('data')
    # Check database, returns None if there is no row
    # cached_location is a Location object, not just the data
    cached_location = Location.query.filter_by(search_query=query).first()

    if cached_location:
        return jsonify(cached_location.to_dict())
    else:
        location_entry = Location.create_entry(query)
        db.session.add(location_entry)
        db.session.commit()
        return jsonify(location_entry.to_dict())


@app.route('/weather')
def weather_route():
    latitude = request.args.get('data[latitude]')
    longitude = request.args.get('data[longitude]')
    result = Weather.create_entry(latitude, longitude)
    return jsonify(result.dailies)


@app.route('/yelp')
def yelp_route():
    query = request.args.get('data[search_query]')
    result = Yelp.create_entry(query)
    return jsonify(result.restaurants)


@app.route('/events')
def events_route():
    query = request.args.get('data[formatted_query]')
    result = Events.create_entry(query)
    return jsonify(result.events)


@app.route('/movies')
def movies_route():
    query = request.args.get('data[search_query]')
    result = Movies.create_entry(query)
    return jsonify(result.movies)


@app.route('/trails')
def trails_route():
    latitude = request.args.get('data[latitude]')
    longitude = request.args.get('data[longitude]')
    result = Trails.create_entry(latitude, longitude)
    return jsonify(result.trails)


from app.models.location import Location
from app.models.weather import Weather
from app.models.yelp import Yelp
from app.models.events import Events
from app.models.movies import Movies
from app.models.trails import Trails
