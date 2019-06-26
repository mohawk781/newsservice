import json
from flaskr.models import News

from flask import (Blueprint, request)

bp = Blueprint('request', __name__)


def find_article(filters):
    article = News.query.filter_by(**filters).all()
    return article


@bp.route('/request', methods=['GET', 'POST'])
def requestdb():
    data = []
    filters = {}
    if request.json['tag'] != "":
        filters.update({"tag": request.json['tag']})

    if request.json['author'] != "":
        filters.update({"author": request.json['author']})

    if request.json['title'] != "":
        filters.update({"title": request.json['title']})

    if request.json['text'] != "":
        filters.update({"text": request.json['text']})

    if request.json['facilityid'] != "":
        filters.update({"facilityid": request.json['facilityid']})

    articles = find_article(filters)
    for article in articles:
        if article.time <= request.json['older']:
            data.append({'title': article.title, 'author': article.author, 'time': article.time, 'tag': article.tag, 'text': article.text, 'facilityid': article.facilityid})

    return json.dumps(data)
