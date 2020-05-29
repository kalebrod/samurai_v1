from flask_restful import Resource,reqparse
from flask import jsonify
# from flask_login import current_user,login_user,logout_user

from app import api
from app import modules

#  from app import login_manager

class Register(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
    
    def put(self):
        self.parser.add_argument('id')
        self.parser.add_argument('email')
        self.parser.add_argument('senha')
        self.parser.add_argument('nome')

        new_user = self.parser.parse_args()
        response = modules.register_user(new_user)

        if response:
            return {"message":"SUCCESS"}, 200
        else:
            return {"message":"FAILED"}, 400 # Bad Request



class Login(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('senha')
        self.parser.add_argument('id')
    
    def post(self):
        #if current_user.is_authenticated:
        #   return {'status':'user is loged'}, 200

        query  = self.parser.parse_args()
        response = modules.check_user(query)

        if not response:
            # login_user(user)
            return {"message":"FAILED"}, 404 # Not found

        else:
            return response


# login_manager.login_view = Login
api.add_resource(Login,'/api/login',endpoint='login')
api.add_resource(Register,'/api/register',endpoint='register')