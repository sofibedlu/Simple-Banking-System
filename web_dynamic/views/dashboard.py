#!/usr/bin/python3
"""define the Banker dashboard route"""

from web_dynamic.views import app_views
from flask import Flask, render_template, make_response, request
from flask_login import login_required, current_user


@app_views.route('/dashboard', methods=['POST', 'GET'], strict_slashes=False)
@login_required
def dash():
    """return Banker dashboard"""

    user = current_user
    path = request.path

    response = make_response(render_template('dashboard.html', user=user, path=path))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
