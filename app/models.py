from app import db


class Location(db.model):
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(256), unique=True)
    formatted_query = db.Column(db.String(256))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def to_dict(self):
        return {
            'query' = self.query,
            'formatted_query' = self.formatted_query,
            'latitude' = self.latitude,
            'longitude' = self.longitude
        }
