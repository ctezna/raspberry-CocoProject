from cocoProject import app, db
from cocoProject.camera_pi import Camera
from flask import render_template, Response


@app.route("/")
def init():
    return "Welcome to The Coco Project IoT module."

@app.route("/feed")
def feed():
    return "This will activate the food dispenser."

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/camera")
def camera():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')