#!/usr/bin/python3
"""return Customer"""

from api.v1.views import app_views
from flask import abort, request

@app_views.route('/customer', methods=['GET'], strict_slashes=False)
def login():
    pass
