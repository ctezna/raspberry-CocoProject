from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from gpiozero import OutputDevice
import board
import neopixel

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
motor = OutputDevice(4)
pixels = neopixel.NeoPixel(board.D18, 24)

from cocoProject import routes, models