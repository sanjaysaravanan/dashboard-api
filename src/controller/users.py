""" Users Endpoint """

from flask import request
from flask_restx import Namespace, Resource

from schema.user_fields import create_user, login_user
from service.users import Users

NS = Namespace(
    "api/users",
    description='Operations related to users'
)

CREATE_USER = NS.model("createUser", create_user())
LOGIN_USER = NS.model("loginUser", login_user())


@NS.route("/login")
class UserLogin(Resource):
    """ User Login """

    @NS.expect(LOGIN_USER, validate=True)
    def post(self):
        """ Login a user on valid credential """
        return Users().login_user(request.json)


@NS.route("/create-user")
class UserCreate(Resource):
    """ User Creation """

    @NS.expect(CREATE_USER, validate=True)
    def post(self):
        """ Creates a user """
        return Users().create_user(request.json)


@NS.route("/<string:email>")
class UserCollection(Resource):
    """ Users Collection """

    def get(self, email):
        """ Return a user with email """
        return Users().get_user(email)

    def delete(self, email):
        """ Deletes a user with email """
        return Users().delete_user(email)
