from random import *
from flask import Blueprint
from flask_restful import Api, Resource

api_bp = Blueprint('api', __name__)


class Random(Resource):
    def get(self):
        return {'randomNumber': randint(1, 100)}


api = Api(api_bp)
api.add_resource(Random, '/random')
