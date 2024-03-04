from flask import Blueprint, request, jsonify
from .spider import BasicSpider

spider_bp = Blueprint('spider_bp', __name__)

@spider_bp.route('/parse_query', methods=['POST', 'GET'])
def get_links():
  if request.method == 'POST':

    # Storing the input query form the user
    query = request.get_json()['query']

    # web crawler instance
    spider = BasicSpider("links")

    # Crawl links and headers from query
    links = spider.get_data(query=query)

    return jsonify(links), 200