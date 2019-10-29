from cocoProject import db, app
from cocoProject.models import Light

if __name__ == "__main__":
    with app.app_context():
        light = Light.query.first()
        light.status = True
        db.session.commit()
