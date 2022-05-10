""" Service Users Endpoint """
from passlib.hash import pbkdf2_sha256 as sha256

from service.base import Base


# pylint: disable=broad-except
# pylint: disable=unused-variable
class Users(Base):
    """ Service for Users """

    def create_user(self, data):
        """ Create a user """
        try:
            email_item = self.collection.find_one(
                {"email": data["email"]}, {"_id": 0})
            if email_item:
                return {
                    "errorMsg": "Email already exists, "
                                "login or sign up with different email-Id"
                }, 409
            data["password"] = sha256.hash(data["password"])
            self.collection.insert_one(data)
            return {
                "message": "User created successfully, Try login!!!"
            }, 201
        except Exception as ex:
            return {
                "errorMsg": "Something went wrong, please try after some time"
            }, 500

    def login_user(self, data):
        """ Login a User """
        try:
            email_db_item = self.collection.find_one(
                {"email": data["email"]}, {"_id": 0})
            if not email_db_item:
                return {
                    "errorMsg": "No user found with email {}".format(
                        data["email"])
                }, 404

            if sha256.verify(data["password"], email_db_item["password"]):
                return {
                    "message": "Logged in successfully!"
                }, 200

            return {
                "errorMsg": "Invalid password, please try again"
            }, 401
        except Exception as ex:
            return {
                "errorMsg": "Sorry for the inconvenience, try after sometime."
            }, 500

    def delete_user(self, email):
        """ Deletes a user """
        return "Coming Soon"

    def get_user(self, email):
        """ Return details of a user """
        try:
            item = self.collection.find_one(
                {"email": email}, {"_id": 0, "password": 0})
            if not item:
                return {
                    "errorMsg": "user with email {} not found".format(email)
                }, 404
            return item, 200
        except Exception as ex:
            return {
                "errorMsg": "Sorry for the inconvenience, try after sometime."
            }, 500
