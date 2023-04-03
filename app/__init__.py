from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
import os

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()


def create_app(static_url_path="", static_folder="static"):
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'stocks.db')
    app.config['SECRET_KEY']='123456'
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    
    from app.stocks import bp as stocks_bp
    app.register_blueprint(stocks_bp)


    return app

from app import models 