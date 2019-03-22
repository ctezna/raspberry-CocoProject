from cocoProject import app, db, static

@app.route("/")
def init():
    return static/Logo_big.png