from flask import Flask, request
from config import Config
from gpiozero import OutputDevice
import board
import neopixel

app = Flask(__name__)
app.config.from_object(Config)
motor = OutputDevice(4)
pixels = neopixel.NeoPixel(board.D18, 24)

from cocoProject import routes