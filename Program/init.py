from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, "users.db")
app.config['SECRET_KEY'] = '123456'


db = SQLAlchemy(app)

from .models import User




from Program import forms
from Program import routes


if __name__ == "__main__":
    app.run(debug=True)