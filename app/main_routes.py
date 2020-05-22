# from flask import Blueprint
from app import app

# main = Blueprint('main',__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'