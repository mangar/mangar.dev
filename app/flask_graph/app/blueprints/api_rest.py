from flask import Blueprint, request

blueprint = Blueprint('api-rest', __name__, url_prefix='/api-rest')



@blueprint.route('/customer/<int:customer_id>', methods=['GET'])
def customer(customer_id):
    return {
        'mesage': 'Message for /api-rest/customers',
        'customer_id': customer_id
    }
