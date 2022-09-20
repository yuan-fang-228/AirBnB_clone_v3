#!/usr/bin/python3
"""index page show status"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


classes = {"Amenity": amenities, "City": cities,
           "Place": places, "Review": reviews, "State": states, "User": users}


@app_views.route("/status")
def status():
    """show the status OK"""
    return jsonify({"status": "OK"})


@app_views.route("/api/v1/stats")
def show_stats():
    """show the number of each objects by type"""
    results = {}
    for key, value in classes.items():
        result[value] = storage.count(key)
    return jsonify(results)
