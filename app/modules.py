
from sqlalchemy.inspection import inspect
from werkzeug.security import check_password_hash

from app import db
from app.models import User


toJSON = lambda query : {c: getattr(query,c) for c in inspect(query).attrs.keys()}

def check_user(user):
    query = User.query.get(user['id'])

    if query != None and check_password_hash(query.senha,user['senha']):
        return {'status':True,'message':'User login succesfully'},query.id

    else:
        return {'status':False,'message':'User login falied'},None

def register_user(request):
    new_user = User(
        id = request['id'],
        email = request['email'],
        unhashed = request['senha'],
        nome = request['nome']
    )
    db.session.add(new_user)
    db.session.commit()

    return {'status':True,'message':'Sign in succesfully'}
