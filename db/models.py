from db.database import db


class Dispenser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flow_volume = db.Column(db.Float, primary_key=True)
