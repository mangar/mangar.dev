import os
import click


class Config(object):
    ENV = os.environ["ENV"] if "ENV" in os.environ else "DEVELOPMENT"
    CSRF_ENABLED = True
    SECRET_KEY = "this_is_a_secret_key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:pwd@192.168.1.113/py_mysql"
    click.echo(SQLALCHEMY_DATABASE_URI)


class TestingConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql://root:pwd@192.168.1.113/py_mysql"
