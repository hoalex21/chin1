import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "<h1>学中文</h1> <h2>学中文</h2> <h3>学中文</h3> <h4>学中文</h4> <h5>学中文</h5> <h6>学中文</h6> <p>学中文</p> \
            <h1>hi</h1> <h2>hi</h2> <h3>hi</h3> <h4>hi</h4> <h5>hi</h5> <h6>hi</h6> <p>hi</p>"

    return app
