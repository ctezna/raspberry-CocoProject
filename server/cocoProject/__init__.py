from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


from cocoProject import routes, models