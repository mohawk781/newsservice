import os
from newsservice.db import db_session, init_db
from flask_bootstrap import Bootstrap

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    Bootstrap(app)
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

    from newsservice import index
    app.register_blueprint(index.bp)

    from newsservice import savenews
    app.register_blueprint(savenews.bp)

    from newsservice import requestnews
    app.register_blueprint(requestnews.bp)

    from newsservice import latestnews
    app.register_blueprint(latestnews.bp)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
