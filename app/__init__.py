from flask import Flask
import os
from config import basedir


app = Flask(__name__)


from app import views, models
