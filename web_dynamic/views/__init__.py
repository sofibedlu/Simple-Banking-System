#!/usr/bin/python3
""" Blueprint for the App """
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from web_dynamic.views.dashboard import *
from web_dynamic.views.login import *
from web_dynamic.views.home import *
from web_dynamic.views.auth import *
from web_dynamic.views.base import *
from web_dynamic.views.signup import *
from web_dynamic.views.logout import *
