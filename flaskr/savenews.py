from datetime import datetime

from flaskr.db import db_session
from flaskr.models import News
from flaskr.auth import auth

from flask import (Blueprint, request)
from flaskr.db import init_db

bp = Blueprint('save', __name__)


@bp.route('/save', methods=['GET', 'POST'])
def save():
    init_db()
    articlejson = request.json['news']
    article = News(articlejson[0], articlejson[1], datetime.now().strftime('%Y-%m-%d %H:%M:%S'), articlejson[2], articlejson[3])
    if auth(articlejson[4], articlejson[5]) == "1":
        db_session.add(article)
        db_session.commit()
        log = "The Article: '{}' was added.".format(articlejson[0])
    else:
        log = "You do not have the permission to post News"

    return log
