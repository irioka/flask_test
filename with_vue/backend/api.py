from random import randint
from flask import Blueprint, jsonify, make_response, request
from flask_restful import Api, Resource, reqparse
from backend.models import TaskModel, db

api_bp = Blueprint('api', __name__)


class Random(Resource):
    def get(self):
        return {'randomNumber': randint(1, 100)}


class TaskListAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title', type=str, help='Title')
        self.parser.add_argument('text', type=str, help='Text')
        # super(TaskListAPI, self).__init__()

    def get(self):
        tasks = TaskModel.query.order_by(TaskModel.id.desc()).all()
        tasks_dict = [task.to_dict() for task in tasks]
        return jsonify(tasks_dict)

    def post(self):
        args = self.parser.parse_args()
        task = TaskModel(title=args['title'], text=args['text'])
        db.session.add(task)
        db.session.commit()
        task = TaskModel.query.order_by(TaskModel.id.desc()).first()
        id = str(task.id)
        r = make_response(id)
        return r


class TaskAPI(Resource):
    def delete(self, id):
        task = TaskModel.query.get(id)
        db.session.delete(task)
        db.session.commit()
        r = make_response(id)
        return r


api = Api(api_bp)
api.add_resource(Random, '/random')
api.add_resource(TaskListAPI, '/task')
api.add_resource(TaskAPI, '/task/<id>')
