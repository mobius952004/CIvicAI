from flask import Flask
from app.routes.voice_routes import voice_bp

def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_object('app.config.Config')

    # Register blueprints
    app.register_blueprint(voice_bp, url_prefix="/api")

    return app