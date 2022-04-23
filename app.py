import os
from flask import Flask
from http_methods import server


def create_app():

    app = Flask(__name__)
    app.register_blueprint(server.bp)
    return app


app = create_app()


if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    os.environ['FLASK_APP'] = 'app'
    app.run()
