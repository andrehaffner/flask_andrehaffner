from flask import Flask


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['SECRET_KEY'] = "as@d145!sidh12*G3478"
    app.config['SEND_FILE_MAX_AGE'] = 0
    from .views import Views
    app.register_blueprint(Views, url_prefix='/')
    return app
