""" Graph generation Endpoint """

from fastapi import Body
from flask import request
from flask_restx import Namespace, Resource, reqparse
from numpy import true_divide

from service.graph_generation import GraphGeneration
from werkzeug.datastructures import FileStorage

from schema.graph_gen_fields import report

upload_parser = reqparse.RequestParser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)
upload_parser.add_argument('name', type=str, location='form')

NS = Namespace(
    'generate-graph',
    description='Operations related to tiles'
)

REPORT = NS.model("Report", report())


@NS.route("")
class GenerateGraph(Resource):
    """ Graph Generation """
    @NS.expect(upload_parser)
    def post(self):
        """ Return file location to Service """
        args = upload_parser.parse_args()
        print(request.form.get('data'))
        return GraphGeneration().file_to_dataframe(
            args.get("file", ""), request.files)
