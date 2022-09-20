#!/usr/bin/python3
"""index page show status"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status():
    """show the status OK"""
    return jsonify({"status": "OK"})
