from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

class PainRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pain_score = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    weather = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f'<PainRecord {self.id}>'
