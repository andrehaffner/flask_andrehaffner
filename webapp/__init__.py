from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask import Flask
from os import getenv


load_dotenv()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv("PostgresURI") + "flask_andrehaffner"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "as@d145!sidh12*G3478"
    app.config['SEND_FILE_MAX_AGE'] = 0
    from .views import Views
    app.register_blueprint(Views, url_prefix='/')
    db.init_app(app)
    return app
