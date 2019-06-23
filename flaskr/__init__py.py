import os
from flaskr.db import db_session, init_db

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    init_db()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from flaskr import index
    app.register_blueprint(index.bp)

    from flaskr import savenews
    app.register_blueprint(savenews.bp)

    from flaskr import requestnews
    app.register_blueprint(requestnews.bp)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
