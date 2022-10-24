from flask import Flask
app = Flask(__name__)
from app import views

app.config.from_prefixed_env()
