from flask import Flask, request, redirect


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['SECRET_KEY'] = "as@d145!sidh12*G3478"
    app.config['SEND_FILE_MAX_AGE'] = 0
    from .views import Views
    app.register_blueprint(Views, url_prefix='/')

    @app.before_request
    def before_request():
        if not request.is_secure:
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)

    return app
