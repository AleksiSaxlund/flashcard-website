from os import getenv
from flask import Flask
from db import db
from routes import route

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    app.config["SECRET_KEY"] = getenv("SECRET_KEY")
    app.register_blueprint(route)

    db.init_app(app)

    return app
