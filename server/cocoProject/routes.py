from cocoProject import app, db


@app.route("/")
def init():
    return "Welcome to The Coco Project IoT module."

@app.route("/feed")
def feed():
    return "This will activate the food dispenser."

@app.route("/camera")
def camera():
    return "This will activate the live stream."