""" Todos Endpoint """

from flask import request
from flask_restx import Namespace, Resource

from schema.todo_fields import todo
from service.todos import Todos

NS = Namespace(
    'api/todos',
    description='Operations related to tiles'
)

TODO = NS.model("Todo", todo())


@NS.route("")
class TodosCollection(Resource):
    """ Todos Collection methods """

    def get(self):
        """ Returns list of all todos """
        return Todos().get_todos()


@NS.route("/<string:email>")
class TodosEmail(Resource):
    """ Todos Collection by email """

    def get(self, email):
        """ Returns all the todos with a email """
        return Todos().get_todos_email(email)

    @NS.expect(TODO, validate=True)
    def post(self, email):
        """ Creates a new todos """
        return Todos().create_one(email, request.json)


@NS.route("/<string:email>/<string:todo_id>")
class TodosItemId(Resource):
    """ Todos collection by id """

    def get(self, email, todo_id):
        """ Returns Todo with a id """
        return Todos().get_one(email, todo_id)

    @NS.expect(TODO, validate=True)
    def put(self, email, todo_id):
        """ Updates a todo with id """
        return Todos().update_one(email, request.json, todo_id)

    def delete(self, email, todo_id):
        """ Delete a todo with a id """
        return Todos().delete_one(email, todo_id)
