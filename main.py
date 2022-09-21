from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from views import views


def create_app(database):
    uri = 'postgresql+psycopg2://hafftech:mZMjoh792mXPwAr1McyP@' \
          'hafftech.c1smrictv5up.sa-east-1.rds.amazonaws.com/andrehaffner'
    webapp = Flask('flask')
    webapp.config["SQLALCHEMY_DATABASE_URI"] = uri
    webapp.register_blueprint(views, url_prefix="/")
    webapp.config["SECRET_KEY"] = "asdfiohbasdfofhjxcg"
    webapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    database.init_app(webapp)
    return webapp


if __name__ == '__main__':
    Database = SQLAlchemy()
    WebApp = create_app(Database)
    WebApp.run(debug=True)
