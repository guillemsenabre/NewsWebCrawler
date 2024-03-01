from flask import Blueprint, render_template

spider_bp = Blueprint('spider_bp', __name__)

@spider_bp.route('/get_links')
def get_links():
  pass