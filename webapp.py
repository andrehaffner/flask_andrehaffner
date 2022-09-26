from flask_sqlalchemy import SQLAlchemy
from flask import Flask


def create_webapp(database):
    app = Flask(__name__, template_folder='templates')
    postgres_uri = 'postgresql+psycopg2://hafftech:mZMjoh792mXPwAr1McyP@' \
                   'hafftech.c1smrictv5up.sa-east-1.rds.amazonaws.com/andrehaffner'
    from views import views
    app.register_blueprint(views, url_prefix="/")
    app.config["SECRET_KEY"] = "as@d145!sidh12*G3478"
    app.config["SQLALCHEMY_DATABASE_URI"] = postgres_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    database.init_app(app)
    return app


database = SQLAlchemy()
if __name__ == '__main__':
    webapp = create_webapp(database)
    webapp.run(port=1808, debug=True)
