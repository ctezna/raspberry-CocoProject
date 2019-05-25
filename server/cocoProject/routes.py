from cocoProject import app, motor
from cocoProject.camera_pi import Camera
from flask import render_template, Response, url_for
from time import sleep
import os


@app.route("/camera")
def init():
    
    return render_template('index.html')

@app.route("/feed")
def feed():
    ring("foodShake.mp3")
    motor.on()
    sleep(1.25)
    motor.off()
    return "feed"

@app.route("/ring")
def ring(sound="whistle.wav"):
    ring = os.path.join("cocoProject", "static", "ringtones", sound)
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
        lightOn = os.path.join("cocoProject", "lightOn.py")
        cmd = "sudo python3 " + lightOn
        os.system(cmd)
        return "lightOn"

@app.route("/lightOff")
def lightOff():
        lightOff = os.path.join("cocoProject", "lightOff.py")
        cmd = "sudo python3 " + lightOff
        os.system(cmd)
        return "lightOff"

@app.route("/reboot", methods=['GET','POST'])
def reboot():
        cmd = "sudo reboot"
        os.system(cmd)
        return "rebooted"