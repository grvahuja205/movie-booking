from flask import Blueprint
from flask_rest_jsonapi import Api

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint=api_blueprint)