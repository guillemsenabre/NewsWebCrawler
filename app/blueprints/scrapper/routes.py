from flask import Blueprint, request, jsonify, render_template
from .spider import BasicSpider

spider_bp = Blueprint('spider_bp', __name__)

@spider_bp.route('/search', methods=['POST', 'GET'])
def get_links():
  return render_template('search/search.html')
  '''
  if request.method == 'POST':


    # Storing the input query form the user
    query = request.get_json()['query']

    # web crawler instance
    spider = BasicSpider("links")

    # Crawl links and headers from query
    links = spider.get_data(query=query)
  '''