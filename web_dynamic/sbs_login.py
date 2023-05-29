""" Flask Application """

import secrets
from models import storage
from web_dynamic.controller.auth import login_manager
from os import environ
from flask import Flask, render_template, make_response, jsonify
from web_dynamic.views import app_views

secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.secret_key = secret_key
app.register_blueprint(app_views)
login_manager.init_app(app)



@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """ Main Function """
    host = environ.get('SBS_API_HOST')
    port = environ.get('SBS_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
