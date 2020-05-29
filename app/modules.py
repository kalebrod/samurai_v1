
from sqlalchemy.inspection import inspect
from werkzeug.security import check_password_hash

from app import db
from app.models import User


toJSON = lambda query : {c: getattr(query,c) for c in inspect(query).attrs.keys()}

def check_user(user):
    query = User.query.get(user['id'])

    if query != None and check_password_hash(query.senha,user['senha']):

        user = toJSON(query)
        del user['senha']

        return user

    else:
        False

def register_user(request):
    try:
        new_user = User(
            id = request['id'],
            email = request['email'],
            unhashed = request['senha'],
            nome = request['nome']
        )
        db.session.add(new_user)
        db.session.commit()

        return True

    except:

        return False
