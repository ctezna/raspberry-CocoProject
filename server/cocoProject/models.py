from cocoProject import db


class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    task = db.Column(db.String(20), nullable=False)
    days = db.Column(db.String(100), nullable=False)
    times = db.Column(db.String(64), nullable=False)