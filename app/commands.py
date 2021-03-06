import click
from flask.cli import with_appcontext

from app import db
from .models import User

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    print("Creating tables.....")
    db.create_all()
    print("Tables created.....")