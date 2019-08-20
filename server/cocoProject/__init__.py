from flask import Flask, request
from config import Config
from gpiozero import OutputDevice
from cocoProject.camera_pi import Camera
import os
from time import sleep

app = Flask(__name__)
app.config.from_object(Config)
if Config.HARDWARE != 'pizero':
    camera = Camera()
    motor = OutputDevice(4)
    lightOn = os.path.join("cocoProject", "lights", "rainbow.py")
    cmd = "sudo python3 " + lightOn
    os.system(cmd)
    lightOff = os.path.join("cocoProject", "lights", "lightOff.py")
    cmd = "sudo python3 " + lightOff
    os.system(cmd)
    lightStatus = 0
elif Config.HARDWARE == 'pizero':
    camera = Camera()
    motor = 404
    lightStatus = 0

from cocoProject import routes