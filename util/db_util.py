"""
Handles all database Operations
"""
import os
from pymongo import MongoClient


class DBUtil:
    """
    Handles all database Operations
    """

    db_host = "localhost"
    db_user = "root"
    db_password = "password"
    db_port = 27021
    db_auth_mech = "SCRAM-SHA-1"

    def __init__(self, db_name="todo-api"):
        self.client = MongoClient(
            self.db_host,
            port=self.db_port,
            username=self.db_user,
            password=self.db_password,
            authMechanism=self.db_auth_mech
        )
        self.db_base = self.client[db_name]

    def get_db(self):
        """
        Returns DB
        """
        return self.db_base

    def get_collection(self, collection_name):
        """ Returns collection """
        return self.db_base[collection_name]

    def close_db_conection(self):
        """ Terminate Database connection """
        return self.client.close()
