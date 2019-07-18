from app.location import LocationNormalizer
from app.weather import WeatherNormalizer
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
    try:
        db_check = Location.query.filter_by(search_query=query).first()
        db_check = db_check.to_dict()
    except AttributeError:

        normalized_data = LocationNormalizer(query)
        result = normalized_data.serialize()
        print(result)

        location_entry = Location(
            search_query=result.get('search_query'),
            formatted_query=result.get('formatted_query'),
            latitude=result.get('latitude'),
            longitude=result.get('longitude'))
        db.session.add(location_entry)
        db.session.commit()
        return jsonify(result)

    return jsonify(db_check)


@app.route('/weather')
def weather_route():
    latitude = request.args.get('data[latitude]')
    longitude = request.args.get('data[longitude]')
    result = WeatherNormalizer(latitude, longitude)
    print(result.forecast)
    return jsonify(result.forecast)

from app.models import Location
