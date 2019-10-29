from cocoProject import db


class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    task = db.Column(db.String(20), nullable=False)
    days = db.Column(db.String(100), nullable=False)
    times = db.Column(db.String(64), nullable=False)

class Light(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean)
    red = db.Column(db.Integer, default=255)
    blue = db.Column(db.Integer, default=255)
    green = db.Column(db.Integer, default=255)
    brightness = db.Column(db.Float, default=0.4)