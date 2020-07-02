from random import randint
from flask import Blueprint
from flask_restful import Api, Resource
from backend.models import get_all

api_bp = Blueprint('api', __name__)


class Random(Resource):
    def get(self):
        return {'randomNumber': randint(1, 100)}


class Spam(Resource):
    def get(self):
        return [{'id': x.pk, 'name': x.name, 'note': x.note} for x in get_all()]


api = Api(api_bp)
api.add_resource(Random, '/random')
api.add_resource(Spam, '/spam')
