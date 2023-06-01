#!/usr/bin/python3
"""Define routes for Account"""

from api.v1.views import app_views
from models.account import Account
from flask import abort, jsonify, make_response, request
from models import storage

@app_views.route('/accounts/<account_id>', methods=['GET'], strict_slashes=False)
def get_account(account_id):
    """
    Gets an Account
    """
    account = storage.get(Account, account_id)
    if not account:
        abort(404)

    return jsonify(account.to_dict())


@app_views.route('/accounts/<account_id>', methods=['DELETE'], strict_slashes=False)
def delete_account(account_id):
    """
    Deletes an Account
    """
    account = storage.get(Account, account_id)
    if not account:
        abort(404)
    account.delete()
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/customers/<customer_id>/accounts', methods=['POST'], strict_slashes=False)
def create_account(customer_id):
    """
    Creates an Account
    """

    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    data["customer_id"] = customer_id
    instance = Account(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/accounts/<account_id>', methods=['PUT'], strict_slashes=False)
def update_account(account_id):
    """
    Updates an Account
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    ignore = ['id', 'created_at', 'updated_at']
    account = storage.get(Account, account_id)
    if not account:
        abort(400)

    for key, value in data.items():
        if key not in ignore:
            setattr(account, key, value)
    storage.save()
    return make_response(jsonify(account.to_dict()), 200)
