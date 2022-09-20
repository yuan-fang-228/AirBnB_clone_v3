#!/usr/bin/python3
"""initialise blueprint for flask application"""
from flask import Blueprint
m api.v1.views.index import *


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

