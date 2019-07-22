import json
from newsservice.models import News

from flask import (Blueprint, request)

bp = Blueprint('request', __name__)


@bp.route('/requestnews', methods=['GET', 'POST'])
def requestdb():
    """
    This Method receives filter values as a JSON and uses these to make queries at the database.
    It creates a List with all entries of the database which match the filters.
    Then it converts the list to a JSON document.
    :return: JSON document containing all database entries which matches the filter values.
    """
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
