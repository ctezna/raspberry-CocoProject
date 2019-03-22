from cocoProject import app, db


@app.route("/")
def init():
    return "Welcome to The Coco Project IoT module."