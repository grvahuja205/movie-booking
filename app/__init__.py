from flask import Flask, render_template
from flask_migrate import Migrate
from app.models import db
from app.routes.api import api
from app.routes import screens_view, theater_screen_view

def create_app(settings_path):
    """
    Flask application factory
    :param settings_path: The path to settings file
    :return: The created flask application object
    """

    app = Flask(__name__)

    app.config.from_object(settings_path)

    db.init_app(app)

    Migrate(app, db)

    api.init_app(app)


    @app.route('/')
    def index():
        return render_template('index.html')

    app.register_blueprint(screens_view)
    app.register_blueprint(theater_screen_view)

    return app