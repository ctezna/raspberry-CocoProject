from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from cocoProject.camera_pi import Camera
from cocoProject.light_control import LightControl
#from cocoProject.sound_control import SoundControl
from cocoProject.motor_control import MotorControl
import os, threading
from time import sleep

def _thread_app():
    os.system('sudo $(which python3) /home/pi/IoT-Bootcamp/Project1/code/station.py > \
        /home/pi/logs/tutorial.log 2>&1 &')

def _thread_ngrok():
    os.system('sudo $(which ngrok) http -subdomain=ctezna 5000 > \
        /home/pi/logs/ngrok.log 2>&1 &')

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
lightControl = LightControl()
#soundControl = SoundControl()
from cocoProject.routine_control import RoutineControl
routineControl = RoutineControl()
camera = Camera()
if Config.DEVICETYPE == 'coco': 
    motor = MotorControl(4)
    lightControl.lightSwitch(-2, -2, -2, 0.2)
    lightControl.lightSwitch(0, 0, 0, 0)
elif Config.DEVICETYPE == 'horus':
    threading.Thread(target=_thread_app).start()
    threading.Thread(target=_thread_ngrok).start()
    motor = 404

from cocoProject import routes, models