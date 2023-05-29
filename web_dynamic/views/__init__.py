#!/usr/bin/python3
""" Blueprint for the App """
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from web_dynamic.views.dashboard import *
from web_dynamic.views.login import *