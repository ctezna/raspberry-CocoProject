from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from cocoProject.camera_pi import Camera
from cocoProject.light_control import LightControl
from cocoProject.sound_control import SoundControl
from cocoProject.motor_control import MotorControl
import os
from time import sleep

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
lightControl = LightControl()
soundControl = SoundControl()
camera = Camera()
if Config.DEVICETYPE == 'coco': 
    motor = MotorControl(4)
    lightControl.lightSwitch(-2, -2, -2, 0.2)
    lightControl.lightSwitch(0, 0, 0, 0)
    lightStatus = 0
elif Config.DEVICETYPE == 'horus':
    motor = 404
    lightStatus = 0

from cocoProject import routes, models