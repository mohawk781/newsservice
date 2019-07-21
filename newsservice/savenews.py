from datetime import datetime

from newsservice.db import db_session
from newsservice.models import News
from newsservice.auth import auth

from flask import (Blueprint, request)
from newsservice.db import init_db

bp = Blueprint('save', __name__)


@bp.route('/savenews', methods=['GET', 'POST'])
def save():
    """
    This Method receives a News and a Authentication Token via JSON document. If the check with auth() was successful it
    adds the news to the database. If not it tells the user that the news wasn't added.
    :return: a status wether the News was added or not.
    """
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
        return "The article: '{}' was added.".format(articlejson[0])
    else:
        return 'The news was not posted, as you dont have the permission to post to these facilities: ' + ','.join(facilityidnolist)


def facilityidstringtolist(facilityidstring):
    """
    This method receives a string with the facility id's and converts it to a list with 1 facility id at each index.
    :param facilityidstring: string with all the facility id's
    :return: a list containing the facility id's as strings.
    """
    facilityidlist = facilityidstring.split(",")
    return facilityidlist


def checkifallfacilitiestrue(facilityids, token):
    """
    This method calls the method auth() for each facility id.
    If the User is not a admin at a facility it returns a list containing the facility id.
    :param facilityids: facility id's which auth() should verify
    :param token: Bearer Authentication Token of the User
    :return: list containing the facility id's, where the user is no admin
    """
    facilitylist = []
    for facilityid in facilityids:
        if auth(facilityid, token) != '1':
            facilitylist.append(facilityid)
    return facilitylist
