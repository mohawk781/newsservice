from datetime import datetime

from newsservice.db import db_session
from newsservice.models import News
from newsservice.auth import auth

from flask import (Blueprint, request)
from newsservice.db import init_db

bp = Blueprint('save', __name__)


@bp.route('/savenews', methods=['GET', 'POST'])
def save():
    init_db()
    articlejson = request.json['news']
    facilityids = facilityidstringtolist(articlejson[4])

    if articlejson[0].strip() and articlejson[1].strip() and articlejson[2].strip() and articlejson[3].strip() \
            and articlejson[4].strip() and articlejson[5].strip():
        article = News(articlejson[0], articlejson[1], datetime.now().strftime('%Y-%m-%d %H:%M:%S'), articlejson[2],
                       articlejson[3], articlejson[4])
    else:
        return "No empty fields are allowed in the JSON document."

    facilityidnolist = checkifallfacilitiestrue(facilityids, articlejson[5])
    if not facilityidnolist:
        db_session.add(article)
        db_session.commit()
        log = "The article: '{}' was added.".format(articlejson[0])
    else:
        log = 'The news was not posted, as you dont have the permission to post to these facilities: ' + ','.join(facilityidnolist)

    return log


def facilityidstringtolist(facilityidstring):
    facilityidlist = facilityidstring.split(",")
    return facilityidlist


def checkifallfacilitiestrue(facilityids, token):
    facilitylist = []
    for facilityid in facilityids:
        if auth(facilityid, token) != '1':
            facilitylist.append(facilityid)
    return facilitylist
