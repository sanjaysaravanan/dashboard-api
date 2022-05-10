""" Controller Initialization """

from flask_restx import Api

from .todos import NS as todos_ns
from .users import NS as user_ns
from .reports import NS as reports_ns

API = Api(
    version='0.1.0',
    title='Todos API',
    description='Todos REST API for generic api functionality'
)

API.add_namespace(todos_ns)
API.add_namespace(user_ns)
API.add_namespace(reports_ns)
