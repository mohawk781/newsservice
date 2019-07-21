import json
from flaskr.models import News

from flask import (Blueprint, request)

bp = Blueprint('request', __name__)


@bp.route('/request', methods=['GET', 'POST'])
def requestdb():
    data = []
    articles = News.query.all()

    if request.json['id'] != "":
        articles = [article for article in articles if str(article.id) == request.json['id']]

    if request.json['tag'] != "":
        articles = [article for article in articles if article.tag == request.json['tag']]

    if request.json['author'] != "":
        articles = [article for article in articles if request.json['author'] in article.author]

    if request.json['title'] != "":
        articles = [article for article in articles if request.json['title'] in article.title]

    if request.json['text'] != "":
        articles = [article for article in articles if request.json['text'] in article.text]

    if request.json['facilityid'] != "":
        articles = [article for article in articles if request.json['facilityid'] in article.facilityid]

    if request.json['older'] != "":
        articles = [article for article in articles if article.time <= request.json['older']]

    if request.json['newer'] != "":
        articles = [article for article in articles if article.time >= request.json['newer']]

    for article in articles:
        data.insert(0, {'id': article.id, 'title': article.title, 'author': article.author, 'time': article.time, 'tag': article.tag,
                        'text': article.text, 'facilityid': article.facilityid})

    return json.dumps(data)
