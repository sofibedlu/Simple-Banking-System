#!/usr/bin/python3
"""login route"""

from web_dynamic.views import app_views
from flask_login import login_user
from web_dynamic.controller.verify_banker import verify_credentials
from flask import abort, request, url_for, redirect


@app_views.route('/auth', methods=['POST'], strict_slashes=False)
def auth():

    username = request.form['username']
    password = request.form['password']

    banker = verify_credentials(username, password)

    if banker:
        login_user(banker)
        return redirect(url_for('app_views.dash'))

    return "auth failed"


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
