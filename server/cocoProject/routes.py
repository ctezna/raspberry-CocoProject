from cocoProject import app, db, motor, pixles
from cocoProject.camera_pi import Camera
from flask import render_template, Response, url_for
from time import sleep
import os


@app.route("/camera")
def init():
    
    return render_template('index.html')

@app.route("/feed")
def feed():
    ring()
    motor.on()
    sleep(1.25)
    motor.off()
    return "feed"

@app.route("/ring")
def ring():
    ring = os.path.join("cocoProject", "static", "ringtones", "whistle.wav")
    try:
        cmd = "omxplayer " + ring
        os.system(cmd)
        os.system(cmd)
        pass
    except:
        print("ringtone error")
        pass
    return "ring"

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

@app.route("/lightOn")
def lightOn():
        pixels.fill((255, 255, 255))
        pixles.show()
        return "lightOn"

@app.route("/lightOff")
def lightOff():
        pixels.fill((0, 0, 0))
        pixles.show()
        return "lightOff"

@app.route("/routine", methods=['GET','POST'])
def routine():

        return "saved"