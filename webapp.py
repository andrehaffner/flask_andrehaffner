from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from views import views


def create_application(database):
    uri = 'postgresql+psycopg2://hafftech:mZMjoh792mXPwAr1McyP@' \
          'hafftech.c1smrictv5up.sa-east-1.rds.amazonaws.com/andrehaffner'
    application = Flask('flask')
    application.config["SQLALCHEMY_DATABASE_URI"] = uri
    application.register_blueprint(views, url_prefix="/")
    application.config["SECRET_KEY"] = "as@d145!sidh12*G3478"
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    database.init_app(application)
    return application


if __name__ == '__main__':
    database = SQLAlchemy()
    application = create_application(database)
    application.run(port=1808, debug=True)
