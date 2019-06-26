import os
import pytest

from flaskr.db import Base as _db
from flaskr.models import News
from datetime import datetime


@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database."""
    if os.path.exists('sqlite:///test.sqlite3'):
        os.unlink('sqlite:///test.sqlite3')

    def teardown():
        _db.drop_all()
        os.unlink('sqlite:///test.sqlite3')

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


def test_post_model(session):
    article = News("Title", "Author", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Text",
                   "Tag")

    session.add(article)
    session.commit()

    assert article.id > 0