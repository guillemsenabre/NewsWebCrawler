from flask import Blueprint

scrapper_blueprint = Blueprint('scrapper_blueprint', __name__)

@scrapper_blueprint.route('/scrap_data')
def scrap_data():
  pass


