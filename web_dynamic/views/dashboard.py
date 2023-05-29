#!/usr/bin/python3
"""define the Banker dashboard route"""

from web_dynamic.views import app_views
from flask import Flask, render_template
from flask_login import login_required


@app_views.route('/dashboard', methods=['POST', 'GET'], strict_slashes=False)
@login_required
def dash():
    """return Banker dashboard"""

    return render_template('dashboard.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
