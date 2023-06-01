#!/usr/bin/python3
"""Define routes for Banker"""

from api.v1.views import app_views
from models.banker import Banker
from flask import abort, jsonify, make_response, request
from models import storage
from werkzeug.security import generate_password_hash


@app_views.route('/bankers/<banker_id>', methods=['GET'], strict_slashes=False)
def get_banker(banker_id):
    """
    Gets a Banker
    """
    banker = storage.get(Banker, banker_id)
    if not banker:
        abort(404)

    return jsonify(banker.to_dict())


@app_views.route('/bankers/<banker_id>', methods=['DELETE'], strict_slashes=False)
def delete_banker(banker_id):
    """
    Deletes a Banker
    """
    banker = storage.get(Banker, banker_id)
    if not banker:
        abort(404)
    banker.delete()
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/branches/<branch_id>/bankers', methods=['POST'], strict_slashes=False)
def create_bankers(branch_id):
    """
    Creates a Banker
    """

    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    data["branch_id"] = branch_id
    instance = Banker(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/bankers/<banker_id>', methods=['PUT'], strict_slashes=False)
def update_banker(banker_id):
    """
    Updates a Banker
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    ignore = ['id', 'created_at', 'updated_at']
    banker = storage.get(Banker, banker_id)
    if not banker:
        abort(400)
    
    if "password" in data.keys():
        password = data['password']
        hashed_password = generate_password_hash(password)
        data['password'] = hashed_password
    
    for key, value in data.items():
        if key not in ignore:
            setattr(banker, key, value)
    storage.save()
    return make_response(jsonify(banker.to_dict()), 200)
