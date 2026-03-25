from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    from .config import Config
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    from . import routes
    app.register_blueprint(routes.bp)
    return app

