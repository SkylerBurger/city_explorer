from location import Location
from weather import Weather
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
    locale = request.args.get('data')
    result = Location(locale)
    return jsonify(result.serialize())


@app.route('/weather')
def weather_route():
    latitude = request.args.get('data[latitude]')
    longitude = request.args.get('data[longitude]')
    result = Weather(latitude, longitude)
    return jsonify(result.forecast)
