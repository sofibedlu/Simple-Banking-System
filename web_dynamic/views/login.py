#!/usr/bin/python3
"""login route"""

from web_dynamic.views import app_views
from flask_login import login_user
from web_dynamic.controller.verify_banker import verify_credentials
from flask import abort, request, url_for, redirect


@app_views.route('/login', methods=['POST'], strict_slashes=False)
def login():

    if request.get_json() is None:
        abort(400, description="Not a JSON")

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    banker = verify_credentials(username, password)

    if banker:
        login_user(banker)
        return redirect(url_for('app_views.dash'))

    return "auth failed"


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
