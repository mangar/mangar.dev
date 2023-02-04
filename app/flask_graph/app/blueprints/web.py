from flask import Blueprint, request

blueprint = Blueprint('web', __name__, url_prefix='/')


@blueprint.route("/")
def root():
    return """
    <h1>Flask / GraphQL / Swagger</h1>
    <hr />

    <h2>GraphQL</h2>
    <ul>
        <li><a href='/graphql'>/graphql</a></li>
    </ul>


    <h2>Swagger</h2>
    <ul>
        <li><a href='/doc'>/doc</a></li>
    </ul>


    <h2>api-rest</h2>
    <ul>
        <li><a href='/api-rest/customer/1'>/api-rest/customer/1</a></li>
    </ul>        



    <h2>basic_api</h2>
    <ul>
        <li><a href='/basic_api/hello_world'>/basic_api/hello_world</a></li>
    </ul>     
    """


