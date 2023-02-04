from config import Config

from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy

from app.blueprints.web import blueprint as bp_web
from app.blueprints.basic_api import blueprint as basic_api
from app.blueprints.api_rest import blueprint as bp_api_rest

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(get_environment_config())

    app.register_blueprint(basic_api)
    app.register_blueprint(bp_web)
    app.register_blueprint(bp_api_rest)


    db.init_app(app)


    from app.graphql.schema import schema
    app.add_url_rule('/graphql',
                    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
                    )

    # @app.before_first_request
    # def initialize_database():
    #     db.create_all()

    # @ app.teardown_appcontext
    # def shutdown_session(exception=None):
    #     db.session.remove()



    return app


def get_environment_config():
    if Config.ENV == "TESTING":
        return "config.TestingConfig"
    elif Config.ENV == "DEVELOPMENT":
        return "config.DevelopmentConfig"