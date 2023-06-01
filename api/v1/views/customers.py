#!/usr/bin/python3
"""Define routes for Customer"""

from api.v1.views import app_views
from models.customer import Customer
from flask import abort, jsonify, make_response, request
from models import storage

@app_views.route('/customers', methods=['GET'], strict_slashes=False)
def get_all_customers():
    """
    Gets list of Customer
    """
    customers = storage.all(Customer).values()
    
    list_customers = []
    for customer in customers:
        list_customers.append(customer.to_dict())
    return jsonify(list_customers)


@app_views.route('/customers/<customer_id>', methods=['GET'], strict_slashes=False)
def get_customer(customer_id):
    """
    Gets a Customer
    """
    customer = storage.get(Customer, customer_id)
    if not customer:
        abort(404)

    return jsonify(customer.to_dict())


@app_views.route('/customers/<customer_id>', methods=['DELETE'], strict_slashes=False)
def delete_customer(customer_id):
    """
    Deletes a Customer
    """
    customer = storage.get(Customer, customer_id)
    if not customer:
        abort(404)
    customer.delete()
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/customers', methods=['POST'], strict_slashes=False)
def create_customer():
    """
    Creates a Customer
    """

    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    instance = Customer(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/customers/<customer_id>', methods=['PUT'], strict_slashes=False)
def update_customer(customer_id):
    """
    Updates a Customer
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    ignore = ['id', 'created_at', 'updated_at']
    customer = storage.get(Customer, customer_id)
    if not customer:
        abort(400)

    for key, value in data.items():
        if key not in ignore:
            setattr(customer, key, value)
    storage.save()
    return make_response(jsonify(customer.to_dict()), 200)
