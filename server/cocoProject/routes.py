from cocoProject import app, db, static/Logo_big.png

@app.route("/")
def init():
    return static/Logo_big.png