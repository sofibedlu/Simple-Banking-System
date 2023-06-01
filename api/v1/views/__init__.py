#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.customers import *
from api.v1.views.accounts import *
from api.v1.views.loans import *
from api.v1.views.bankers import *
from api.v1.views.branches import *
