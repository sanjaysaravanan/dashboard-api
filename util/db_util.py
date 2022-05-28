"""
Handles all database functions
"""
import os
from pymongo import MongoClient


class DBUtil:
    """
    Handles all database communications
    """
    db_host = "localhost"
    db_user = "root"
    db_password = "password"
    db_port = 27021
    db_auth_mech = "SCRAM-SHA-1"

    def __init__(self, db_name="todo-api"):
        self.client = MongoClient(
            os.getenv('MONGO_URI')
        )
        self.db_client = self.client[db_name]

    def get_db(self):
        """
        Returns DB client
        """
        return self.db_client

    def get_collection(self, collection_name):
        """ Returns collection """
        return self.db_client[collection_name]

    def close_db_conection(self):
        """ Terminate Database connection """
        return self.client.close()
