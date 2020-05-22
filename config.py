import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Clase que faz alguns setups do flask

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'wbuzttl^a^p6z#2+41ffmvouaqpd8a&dm8(y%#@cgd4a3rn=!8'
     
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///{}'.format(os.path.join(basedir,'app.db'))
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False