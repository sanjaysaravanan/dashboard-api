"""
Handles all database Operations
"""
import os
from dotenv import load_dotenv

from pymongo import MongoClient

load_dotenv()

class DBUtil:
    """
    Handles all database Operations
    """
    db_host = os.getenv('db_host') or "localhost"
    db_user = os.getenv('db_host') or "root"
    db_password = os.getenv('db_host') or "password"
    db_port = os.getenv('db_host') or 27017
    db_auth_mech = "SCRAM-SHA-1"

    def __init__(self, db_name="todo-api"):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db_client = self.client[db_name]

    def get_db(self):
        """
        Returns DB
        """
        return self.db_client

    def get_collection(self, collection_name):
        """ Returns collection """
        return self.db_client[collection_name]

    def close_db_conection(self):
        """ Terminate Database connection """
        return self.client.close()
