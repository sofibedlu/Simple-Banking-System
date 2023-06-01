#!/usr/bin/python3
"""Define routes for Loan"""

from api.v1.views import app_views
from models.branch import Branch
from flask import abort, jsonify, make_response, request
from models import storage

@app_views.route('/branches/<branch_id>', methods=['GET'], strict_slashes=False)
def get_branch(branch_id):
    """
    Gets a Branch
    """
    branch = storage.get(Branch, branch_id)
    if not branch:
        abort(404)

    return jsonify(branch.to_dict())


@app_views.route('/branches/<branch_id>', methods=['DELETE'], strict_slashes=False)
def delete_branch(branch_id):
    """
    Deletes a Branch
    """
    branch = storage.get(Branch, branch_id)
    if not branch:
        abort(404)
    branch.delete()
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/banks/<bank_id>/branches', methods=['POST'], strict_slashes=False)
def create_branch(bank_id):
    """
    Creates a Branch
    """

    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    data["bank_id"] = bank_id
    instance = Branch(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/branches/<branch_id>', methods=['PUT'], strict_slashes=False)
def update_branche(branch_id):
    """
    Updates a Branch
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    ignore = ['id', 'created_at', 'updated_at']
    branch = storage.get(Branch, branch_id)
    if not branch:
        abort(400)

    for key, value in data.items():
        if key not in ignore:
            setattr(branch, key, value)
    storage.save()
    return make_response(jsonify(branch.to_dict()), 200)
