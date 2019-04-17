from cocoProject import app, db
from cocoProject.camera_pi import Camera
from flask import render_template, Response, url_for
from cocoProject.cocoGPIO import feed


@app.route("/camera")
def init():
    return render_template('index.html')

@app.route("/feed")
def feed():
    feed(4,1.5)
    return "feed"

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/cam")
def cam():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')