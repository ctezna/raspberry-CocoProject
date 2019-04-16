from cocoProject import db

class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(20), nullable=False)
    days = db.Column(db.String(7), nullable=False)
    times = db.Column(db.String(20), nullable=False)