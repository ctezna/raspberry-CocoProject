from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from cocoProject.camera_pi import Camera
from cocoProject.light_control import LightControl
from gpiozero import OutputDevice
import os
from time import sleep

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
lightControl = LightControl()
if Config.HARDWARE != 'pizero':
    camera = Camera()
    motor = OutputDevice(4)
    lightControl.lightSwitch(-1, -1, -1, 0.2)
    lightControl.lightSwitch(0, 0, 0, 0)
    lightStatus = 0
elif Config.HARDWARE == 'pizero':
    camera = Camera()
    motor = 404
    lightStatus = 0

from cocoProject import routes, models