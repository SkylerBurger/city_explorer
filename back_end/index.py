from location import Location

from flask import Flask, request, jsonify
from flask_cors import CORS

# TODO: Do I still need this?
from dotenv import load_dotenv
load_dotenv()


# ===
# APP
# ===
app = Flask(__name__)
CORS(app)


# ======
# ROUTES
# ======
@app.route('/location')
def location_route():
    locale = request.args.get('data')
    result = Location(locale)
    return result.serialize()


@app.route('/weather')
def weather_route():
    latitude = request.args.get('data[latitude]')
    longitude = request.args.get('data[longitude]')
    print(latitude, longitude)
    return request.args
