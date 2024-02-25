from flask import Flask
from scrapper.scrapper_routes import scrapper_blueprint

def create_app():
  app = Flask(__name__)

  # Register blueprints
  app.register_blueprint(scrapper_blueprint)

  return app