import logging
from utils.flaskappconfig import flask_config,register_blueprints
from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from utils.config import Config

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt = "%d-%M-%Y %H:%M:%S", level=logging.DEBUG,
    filename="logs.log")

logger = logging.getLogger(__name__)

def create_app():
    '''Creates and configures the flask app'''

    app = Flask(__name__)
    logger.info('Application started')
    flask_config(app)
    api = Api(app)
    jwt = JWTManager(app) 
    register_blueprints(api)
    logger.info('Application ended')
    return app

create_app()