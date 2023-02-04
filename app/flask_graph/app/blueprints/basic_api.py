from flask import Blueprint, request

blueprint = Blueprint('api', __name__, url_prefix='/basic_api')

@blueprint.route('/hello_world')
def hello_world():
    return {'message': 'Hello World!'}

