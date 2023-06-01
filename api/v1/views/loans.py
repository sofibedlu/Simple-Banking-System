#!/usr/bin/python3
"""Define routes for Loan"""

from api.v1.views import app_views
from models.loan import Loan
from flask import abort, jsonify, make_response, request
from models import storage

@app_views.route('/loans/<loan_id>', methods=['GET'], strict_slashes=False)
def get_loan(loan_id):
    """
    Gets a Loan
    """
    loan = storage.get(Loan, loan_id)
    if not loan:
        abort(404)

    return jsonify(loan.to_dict())


@app_views.route('/loans/<loan_id>', methods=['DELETE'], strict_slashes=False)
def delete_loan(loan_id):
    """
    Deletes a Loan
    """
    loan = storage.get(Loan, loan_id)
    if not loan:
        abort(404)
    loan.delete()
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/customers/<customer_id>/loans', methods=['POST'], strict_slashes=False)
def create_loans(customer_id):
    """
    Creates a Loan
    """

    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    data["customer_id"] = customer_id
    instance = Loan(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/loans/<loan_id>', methods=['PUT'], strict_slashes=False)
def update_loan(loan_id):
    """
    Updates a Loan
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    ignore = ['id', 'created_at', 'updated_at']
    loan = storage.get(Loan, loan_id)
    if not loan:
        abort(400)

    for key, value in data.items():
        if key not in ignore:
            setattr(loan, key, value)
    storage.save()
    return make_response(jsonify(loan.to_dict()), 200)
