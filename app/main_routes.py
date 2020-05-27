from flask import render_template,url_for
from app import app

# main = Blueprint('main',__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')