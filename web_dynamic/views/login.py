#!/usr/bin/python3
"""login route"""

from web_dynamic.views import app_views
from flask import render_template
from uuid import uuid4


@app_views.route('/login', methods=['GET'], strict_slashes=False)
def login():
    """return login page for SBS"""

    cache_id = str(uuid4())
    return render_template('login.html', cache_id=cache_id)


if __name__ == "__main__":
    """start flask"""
    app.run(host='0.0.0.0', port=5000)
