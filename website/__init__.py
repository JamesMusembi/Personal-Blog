import imp
from importlib.resources import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import os import path

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "]Ee]zAtR|,U2X~$698rd"
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix= "/")
    app.register_blueprint(auth, url_prefix= "/")
    return app
