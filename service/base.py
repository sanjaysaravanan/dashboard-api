""" Service Base """

import abc
import logging

from util.db_util import DBUtil
from util.utils import ERROR_MSG, snake_case
from fastapi.responses import JSONResponse


class Base(abc.ABC):
    """ Abstract Base class """

    def __init__(self):
        self.class_name = type(self).__name__
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)
    
    def something_went_wrong(self, ex):
        """ Handle Internal Server Error Response """
        print(ex)
        return JSONResponse( status_code=500, content={ "errorMsg": ERROR_MSG } )