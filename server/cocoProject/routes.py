from cocoProject import app, db, motor #, leds
from cocoProject.camera_pi import Camera
from flask import render_template, Response, url_for
from time import sleep
#from rpi_ws281x import *
import pygame, os


@app.route("/camera")
def init():
    pygame.init()
    pygame.mixer.init()
    ring = os.path.join("cocoProject", "static", "ringtones", "whistle.wav")
    try:
        cmd = "omxplayer " + ring
        #os.system('ls')
        os.system(cmd)
        os.system(cmd)
        os.system(cmd)
        os.system(cmd)
        os.system(cmd)
        #pygame.mixer.Sound(ring)
        #pygame.mixer.Sound.play(loops=3)
        pass
    except:
        print("ringtone error")
        pass
    return render_template('index.html')

@app.route("/feed")
def feed():
    motor.on()
    sleep(1.5)
    motor.off()
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

@app.route("/lightOn")
def lightOn():
        #for i in leds.numPixels():
                #leds.setPixelColorRGB(i,255,255,255)
        #leds.show()
        return "lightOn"

@app.route("/lightOff")
def lightOff():
        #for i in leds.numPixels():
                #leds.setPixelColorRGB(i,0,0,0)
        #leds.show()
        return "lightOff"

@app.route("/routine", methods=['GET','POST'])
def routine():

        return "saved"