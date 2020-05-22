from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config

# Instanciando o App
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
#login_manager = LoginManager(app)

api = Api(app)
CORS(app)

from app import api_routes,models,modules,commands,main_routes

app.cli.add_command(commands.create_tables)


