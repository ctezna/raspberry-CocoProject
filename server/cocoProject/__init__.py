from flask import Flask, request
from config import Config
from gpiozero import OutputDevice
import os
from time import sleep

app = Flask(__name__)
app.config.from_object(Config)
motor = OutputDevice(4)
lightOn = os.path.join("cocoProject", "rainbow.py")
cmd = "sudo python3 " + lightOn
os.system(cmd)
lightOff = os.path.join("cocoProject", "lightOff.py")
cmd = "sudo python3 " + lightOff
os.system(cmd)

from cocoProject import routes