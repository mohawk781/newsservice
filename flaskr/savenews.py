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
    facilityids = facilityidstringtolist(articlejson[4])
    article = News(articlejson[0], articlejson[1], datetime.now().strftime('%Y-%m-%d %H:%M:%S'), articlejson[2], articlejson[3], articlejson[4])

    if checkifallfacilitiestrue(facilityids, articlejson[5], articlejson[6]):
        db_session.add(article)
        db_session.commit()
        log = "The Article: '{}' was added.".format(articlejson[0])
    else:
        log = "You do not have the permission to post to all of the facilities"

    return log


def facilityidstringtolist(facilityidstring):
    facilityidlist = facilityidstring.split(",")

    return facilityidlist


def checkifallfacilitiestrue(facilityids, token, memberid):
    for facilityid in facilityids:
        if auth(facilityid, token, memberid) == 0:
            return False
    return True
