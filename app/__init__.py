from flask import Flask
from app.blueprints.main.routes import main_bp

def create_app():
  app = Flask(__name__)

  # Register blueprints
  app.register_blueprint(main_bp)


  return app