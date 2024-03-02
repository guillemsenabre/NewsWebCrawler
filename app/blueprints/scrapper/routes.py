from flask import Blueprint, request, jsonify

spider_bp = Blueprint('spider_bp', __name__)

@spider_bp.route('/parse_query', methods=['POST', 'GET'])
def get_links():
  if request.method == 'POST':
    query = request.get_json()
    return jsonify(query), 200