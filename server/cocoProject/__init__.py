from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from gpiozero import OutputDevice

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
motor = OutputDevice(4)


from cocoProject import routes, models