from datetime import datetime

from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin

from app import db
# from app import login_manager

# class User(UserMixin,db.Model):
class User(db.Model):
    id = db.Column(db.String(10),primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    progress = db.Column(db.String(50), nullable = True)


    def __repr__(self):
        return '<User {} - {}'.format(self.id,self.email)
    
    @property
    def unhashed(self):
        raise  AttributeError('Cannot view unhashed password!')

    @unhashed.setter
    def unhashed(self,unhashed):
        self.senha = generate_password_hash(unhashed)

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)


    

