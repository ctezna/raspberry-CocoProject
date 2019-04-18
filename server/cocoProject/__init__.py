from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from gpiozero import OutputDevice
from rpi_ws281x import *

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
motor = OutputDevice(4)
leds = Adafruit_NeoPixel(24, 18, 800000, 10, False, 255, 0, ws.SK6812W_STRIP)
leds.begin()

from cocoProject import routes, models