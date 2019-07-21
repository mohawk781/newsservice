import json
from newsservice.models import News

from flask import (Blueprint)

bp = Blueprint('latestnews', __name__)


@bp.route('/latestnews', methods=['GET'])
def requestlatestnews():
    """
    This Method queries the last item of the database and convert it to a string.
    :return: A String with the last item of the database
    """
    article = News.query.order_by(News.id.desc()).first()

    latestnews = article.title + '\n' + article.text + '\nby ' + article.author + ' on ' + article.time

    return latestnews


