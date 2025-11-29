from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456'

from Program import forms
from Program import routes
