#!/usr/bin/python3
"""the first endpoint to return API status"""
from flask import Flask, Blueprint, render_template
from storage import models
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_currentsession(exc):
    """remove current session"""
    storage.close()


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", "5000")
    run.app(host=host, port=port, threaded=True)

