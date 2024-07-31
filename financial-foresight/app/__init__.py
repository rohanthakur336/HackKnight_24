# from flask import Flask

# app = Flask(__name__)

# from app import routes

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a1b2c3d4e5f67890abcdef1234567890'

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)

    return app
