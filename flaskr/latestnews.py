import json
from flaskr.models import News

from flask import (Blueprint)

bp = Blueprint('latestnews', __name__)


@bp.route('/latestnews', methods=['GET'])
def requestlatestnews():
    article = News.query.order_by(News.id.desc()).first()

    latestnews = article.title + '\n' + article.text + '\nby ' + article.author + ' on ' + article.time

    return latestnews


