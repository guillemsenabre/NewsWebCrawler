from flask import Blueprint, request, jsonify, render_template
from .spider import BasicSpider

spider_bp = Blueprint('spider_bp', __name__)

@spider_bp.route('/search', methods=['POST', 'GET'])
def get_links():
  
#  if request.method == 'POST':
    
  # Storing the input query form the user
  query = request.form.to_dict()

  # web crawler instance
  spider = BasicSpider("links")

  # Crawl links and headers from query
  data = spider.get_data(query=query)


  print(data)

  return render_template('search/search.html', data=data)