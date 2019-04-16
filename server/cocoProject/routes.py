from cocoProject import app, db, motor
from cocoProject.camera_pi import Camera
from flask import render_template, Response, url_for
from cocoProject.cocoGPIO import feed
from time import sleep


@app.route("/camera")
def init():
    return render_template('index.html')

@app.route("/feed")
def feed():
    motor.on()
    sleep(3)
    motor.off()
    return 0

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