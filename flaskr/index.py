from flask import render_template
import http.client
from flaskr.models import News
from flask import (Blueprint)

bp = Blueprint('index', __name__)


def isonline():
    try:
        conn = http.client.HTTPConnection("openstack.cebitec.uni-bielefeld.de")
        conn.request("HEAD", "/")
        r1 = conn.getresponse()
        if int(r1.status) == 302:
            print(r1.status)
            return "online"
        else:
            return "offline"
    except IOError:
        return "offline"


@bp.route('/')
def render():
    online = isonline()
    return render_template("index.html", news=News.query.all(), online=online)
