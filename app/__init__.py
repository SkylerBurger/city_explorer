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
    # Check database, returns None if there is no row
    db_check = Location.query.filter_by(search_query=query).first()

    if db_check:
        return jsonify(db_check)
    else:
        location_entry = Location.create_entry(query)
        db.session.add(location_entry)
        db.session.commit()
        return jsonify(location_entry.to_dict())


@app.route('/weather')
def weather_route():
    latitude = request.args.get('data[latitude]')
    longitude = request.args.get('data[longitude]')
    result = WeatherNormalizer(latitude, longitude)
    return jsonify(result.forecast)


@app.route('/events')
def events_route():
    formatted_query = request.args.get('data[formatted_query]')


from app.models import Location
