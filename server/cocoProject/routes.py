from cocoProject import app, db
from cocoProject.static import Logo_big.png

@app.route("/")
def init():
    return Logo_big.png