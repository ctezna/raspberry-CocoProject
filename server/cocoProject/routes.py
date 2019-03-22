from cocoProject import app, db

@app.route("/")
def init():
    return static/Logo_big.png