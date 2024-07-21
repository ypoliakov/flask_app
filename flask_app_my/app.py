from flask import Flask, g
from database import init_db, get_db, close_db
from routes import init_routes


def create_app():
    app = Flask(__name__)

    @app.before_request
    def before_request():
        g.db = get_db()

    @app.teardown_appcontext
    def teardown_db(exception):
        close_db()

    with app.app_context():
        init_db(app)

    init_routes(app)

    return app
