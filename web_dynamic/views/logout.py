#!/usr/bin/python3
"""logout banker"""

from flask_login import logout_user
from web_dynamic.views import app_views
from flask import url_for, redirect
from flask_login import login_required


@app_views.route('/logout', methods=['GET'], strict_slashes=False)
@login_required
def logout():
    logout_user()
    # Redirect to the login page
    return redirect(url_for('app_views.login'))


if __name__ == "__main__":
    """start flask"""
    app.run(host='0.0.0.0', port=5000)
